
#metodos

l = []

#append
l.append(10)
l.append([2,3])
print(l)

#extend
l.extend([2,3])
print(l)

#insert
lista_ordenada = [7,15,15,25,50]
lista_ordenada.insert(0, 2)
print(lista_ordenada)

#remove
lista_ordenada.remove(15)
print(lista_ordenada)

#pop

lista_ordenada.pop(0)
print(lista_ordenada)

#funções

#len
print(len(lista_ordenada))

#list - construtor
nome = "Weuler"
print(nome[2])

#max/min

print(min(lista_ordenada))