#leia 2 valores (inteiros) 
# e mostre a soma dos numeros impares entre eles

a = int(input()) #10
b = int(input()) #7

inicio = min(a,b)
fim = max(a,b)

#acumulador
soma = 0

for numero in range(inicio, fim):
    if numero % 2 == 1:
        soma += numero

print(soma)