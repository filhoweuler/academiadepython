#ler um inteiro "n" do teclado
n = int(input())

#criar uma lista
lista = []

#nas n linhas seguintes, ler um inteiro em cada
for i in range(n):
    numero = int(input())
    lista.append(numero)

#imprimir a média dos inteiros lidos
print( sum(lista) / n )