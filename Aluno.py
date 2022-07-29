class Aluno:

    def __init__(self,nome,respostas):
        self.nome = nome
        self.respostas = respostas

    def calcularMedia(self,gabarito):
        self.nota = 0
        for letra in self.respostas:
            if(letra != self.respostas[0]):
                break
        
        for i in range(len(self.respostas)):
            if self.respostas[i] == gabarito[i]:
                self.nota += 1
        return self.nota
