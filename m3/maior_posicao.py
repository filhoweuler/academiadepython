#dado n, seguido de n numeros (float) [-1000, 1000], 
# encontre o maior e a posição
n = int(input())

# maior = -1001
# posicao = 0

# for i in range(n):
#     #repete n vezes
#     numero = float(input())
#     if numero > maior:
#         #sempre entra na primeira iteração
#         maior = numero
#         posicao = i

l = []
for i in range(n):
    numero = float(input())
    l.append(numero)

maior = max(l)
posicao = l.index(maior)

print(maior)
print(posicao)
