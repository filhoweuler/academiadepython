#dado n (inteiro), imprima todos os numeros pares 
# entre 1 e n (inclusive)
n = int(input())

# for numero in range(1,n+1):
#     if numero % 2 == 0:
#         #é par
#         print(numero)

for numero in range(2, n+1, 2):
    print(numero)