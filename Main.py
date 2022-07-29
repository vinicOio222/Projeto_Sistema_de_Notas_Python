from Cadeira import Cadeira

nome = input("Insira o nome do Curso: ")

C = Cadeira(nome)
C.criarDir()

while True:
    print("Bem-vindo(a) ao Sistema de Notas da Universidade Estadual do Ceará (UECE)\n"
         +"-> Curso selecionado: " + nome + "\n\n"
         +"1.Adicionar Cadeira e Alunos;\n"
         +"2.Adicionar Gabarito;\n"
         +"3.Gerar o Resultado da Turma;\n"
         +"4.Listar Cadeiras e Alunos Matriculados;\n"
         +"5.Listar Resultados;\n"
         +"6.Listar Gabaritos das Cadeiras;\n"
         +"0.Sair;\n")

    op = int(input("Selecione uma operação que deseja realizar: "))
    match op:
        case 0:
            C.limparTela()
            print("Encerrando o sistema...")
            break 

        case 1:
            C.limparTela()
            C.criarCadeira()
            C.limparTela()

        case 2:
            C.limparTela()
            C.respostasGabarito()
            C.limparTela()
        
        case 3:
            C.limparTela()
            C.criarResultados()
            print("\n")
        
        case 4:
            C.limparTela()
            C.mostrarCadeiras()
            print("\n")
        
        case 5:
            C.limparTela()
            C.listarResultados()
            print("\n")
        
        case 6:
            C.limparTela()
            C.mostrarGabaritos()            
            print("\n")
        
        case _:
            
            print("Operação Inexistente! Tente novamente.")
