from operator import attrgetter
import os
from Aluno import Aluno

class Cadeira:

    def __init__(self,curso):
        self.curso = curso
        self.listaNotas = []
        self.listaNomes = []
    
    def criarDir(self):
        try:
           os.makedirs(self.curso + "/Cadeiras")
           os.makedirs(self.curso + "/Resultados/Discentes")
           os.makedirs(self.curso + "/Resultados/Notas")
           os.makedirs(self.curso + "/Gabaritos")
        except FileExistsError:
           pass
            
    def limparTela(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def criarCadeira(self):
        nomeCadeira = input("Insira o nome da cadeira: ")
        f = open(self.curso + "/Cadeiras/" + nomeCadeira + ".txt", "w")

        while True:
            try:
                nomeAluno = input("Insira o nome do aluno: ")
                gabarito = input("Insira o gabarito do aluno (V ou F - 10 questões): ").upper()
                dados = ""

                if len(gabarito) == 10:
                    dados+=  nomeAluno + "\t" + gabarito + "\n"
                elif len(gabarito)>10:
                    print("Número de questões além do permitido!")
                else:
                    print("Há questões não respondidas!")
               
                with open(self.curso + "/Cadeiras/" + nomeCadeira + ".txt", "a") as f:
                   f.write(dados)
                   f.close()
            except IOError:
                print("Erro no registro de dados...")
            else:
                print("Dados registrados!")

            op = int(input("Deseja adicionar mais alguém ao sistema ?\n1.Sim;\t2.Não;\n"))
            if op == 2:
                break

    def mostrarCadeiras(self):
        print("----- Lista de Cadeiras -----")
        for file in os.listdir(self.curso + "/Cadeiras/"):
            nomeC = file.split(".",1)[0]
            print("----- Cadeira: "+ nomeC + " ------")
            try:
                with open(self.curso + "/Cadeiras/" + file,"r") as f:
                   print(f.read())
                   print("\n")
            except FileNotFoundError:
                   print("Arquivo não encontrado...")
            except IOError:
                   print("Erro na leitura de dados...")

    def respostasGabarito(self):
        dados = ""
        nomeGabarito = input("Insira o nome gabarito da cadeira: ")
        gabarito = open(self.curso +"/Gabaritos/" + nomeGabarito + ".txt" , "w")
        respostasG = input("Insira o gabarito da prova: ")
        dados += respostasG
        if len(dados) == 10:
            try:
                with open(self.curso + "/Gabaritos/" + nomeGabarito + ".txt", "a") as f:
                   f.write(dados)
                   f.close()
            except FileNotFoundError:
                print("Arquivo não encontrado...")
            except IOError:
                print("Erro no registro de arquivos...")
            else:
                print("Dados lidos com sucesso!")

    def mostrarGabaritos(self):
        print("----- Lista de Gabaritos -----")
        for file in os.listdir(self.curso + "/Gabaritos/"):
            nomeG = file.split(".",1)[0]
            print("----- Nome do Gabarito: " + nomeG + " -----")

            try:
                with open(self.curso +"/Gabaritos/" + file,"r") as f:
                    print(f.read())
                    print("\n")
            except FileNotFoundError:
                print("Arquivo não encontrado...")
            except IOError:
                print("Erro na leitura dos dados...")
        
    def criarResultados(self):
        cadeira = input("Insira o nome da cadeira: ")
        try:
            dados = ""
            with open(self.curso + "/Cadeiras/" + cadeira + ".txt") as f:
                 dados += f.read()
        except FileNotFoundError:
            print("Arquivo não encontrado...")
        except IOError:
            print("Erro na leitura dos dados...")
        else:
            print("Dados lidos com sucesso!")
        
        linhas = dados.split("\n")
        dados2 = ""
        gabarito = input("Insira o nome do arquivo do gabarito: ")
        try:
            with open(self.curso + "/Gabaritos/" + gabarito + ".txt") as f:
                dados2 += f.read()
        except FileNotFoundError:
            print("Arquivo não encontrado...")
        except IOError:
            print("Erro na leitura dos dados...")
        else:
            print("Dados lidos com sucesso!")
        
        gabaritos = dados2
        try:
            for linha in linhas:
                nomeDiscente = linha.split("\t",1)[0]
                respostasDiscente = linha.split("\t",1)[1]
                self.listaNotas.append(Aluno(nomeDiscente,respostasDiscente))
                self.listaNomes.append(Aluno(nomeDiscente,respostasDiscente))

        except IndexError:
            pass
 
        total = 0
        for i in self.listaNotas:
            i.calcularMedia(gabaritos)
            total += i.nota
        media  = total/len(self.listaNotas)
        media  = float(media)

        total2 = 0
        for i in self.listaNomes:
            i.calcularMedia(gabaritos)
            total2 += i.nota
        media2 = total2/len(self.listaNomes)
        media2 = float(media2)
        print("Média da Turma: " + str(format("%.2f"%media2)))

        out = ""    
        try:
            self.listaNotas.sort(key = attrgetter('nota'),reverse = True)
            for aluno in self.listaNotas:
                out += aluno.nome + "\t" + str(aluno.nota) + "\n"
        
            out += "\n" + "Media da Turma: " + str(format("%.2f"%media))
            f = open(self.curso + "/Resultados/Notas/" + cadeira + ".txt","w")
            with open(self.curso + "/Resultados/Notas/" + cadeira + ".txt", "a") as f:
                f.write(out)
                f.close()
            self.listaNotas.clear()
        except FileNotFoundError:
            print("Arquivo não encontrado...")
        except IOError:
            print("Erro no registro de arquivos...")
        except AttributeError:
            pass
        else:
            print("Dados registrados com sucesso!")
        
        
        out2 = ""
        try:
            self.listaNomes.sort(key = lambda x : x.nome , reverse = False)
            for aluno in self.listaNomes:
                 out2 += aluno.nome + "\t" + str(aluno.nota) + "\n"
            out2 += "\n" + "Media da Turma: " + str(format("%.2f"%media))
            f = open(self.curso + "/Resultados/Discentes/" + cadeira + ".txt" ,"w")
        
            with open(self.curso + "/Resultados/Discentes/" + cadeira + ".txt" ,"a") as f:
                f.write(out2)
                f.close()
            self.listaNomes.clear()
        except FileNotFoundError:
            print("Arquivo não encontrado...")
        except IOError:
            print("Erro no registro de arquivos...")
        except AttributeError:
            pass
        
        out2 = ""


    def listarResultados(self):
        print("----- Lista de Resultados das Turmas -----\n")
        print("==== Ordem Decrescente de Nota ====")
        for file in os.listdir(self.curso +"/Resultados/Notas/"):
            nomeF = file.split(".",1)[0]
            print("----- Cadeira: " + nomeF + " -----")
            try:
                with open(self.curso +"/Resultados/Notas/" + file,"r") as f:
                    print(f.read())
                    print("\n")
            except FileNotFoundError:
                print("Arquivo não encontrado...")
            except IOError:
                print("Erro na leitura dos dados...")

        print("==== Ordem Alfabética ====")
        for file in os.listdir(self.curso +"/Resultados/Discentes/"):
            nomeF = file.split(".",1)[0]
            print("----- Cadeira: " + nomeF + " -----")
            try:
                with open(self.curso +"/Resultados/Discentes/" + file,"r") as f:
                    print(f.read())
                    print("\n")
            except FileNotFoundError:
                print("Arquivo não encontrado...")
            except IOError:
                print("Erro na leitura dos dados...")
