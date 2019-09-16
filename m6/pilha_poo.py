
class Pilha:

    def __init__(self):
        #cria atributo privado na classe
        self.__pl = []

    def empilhar(self, numero):
        self.__pl.append(numero)
    
    def desempilhar(self):
        valor = self.__pl[-1]
        del self.__pl[-1]
        return valor

    def topo(self):
        return self.__pl[-1]

    def vazia(self):
        return len(self.__pl) == 0
    
    def mostrar_pilha(self):
        print(self.__pl)

#Herança

#Criar uma pilha que contem um "somador" e mantem a soma dos numeros na pilha

class PilhaSomadora(Pilha):
    def __init__(self):
        Pilha.__init__(self)
        #dunder -> "double underscore"
        self.__soma = 0

    def soma(self):
        return self.__soma

    #sobrescrita das funções
    def empilhar(self, numero):
        self.__soma += numero
        Pilha.empilhar(self, numero)

    def desempilhar(self):
        valor = Pilha.desempilhar(self)
        self.__soma -= valor
        return valor

pilha = PilhaSomadora()
pilha.empilhar(10)
pilha.empilhar(15)
pilha.empilhar(19)
pilha.mostrar_pilha()
print(pilha.soma())
print(pilha.desempilhar())
print(pilha.soma())
pilha.mostrar_pilha()

