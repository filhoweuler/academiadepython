#leia 10 numeros (inteiro), coloque-os em uma lista 
# e no final mostre as posições da lista 
# que tem numeros menores que 10

numeros = []

for _ in range(10):
    # numero = int(input())
    # numeros.append(numero)
    numeros.append( int(input()) )

# for i in range(10):
#     if numeros[i] < 10:
#         print(numeros[i])

for numero in numeros:
    if numero < 10:
        print(numero)