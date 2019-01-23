#dados 10 valores, conte quantos deles sao positivos 
# e qual a média de todos os valores

#contador
positivos = 0

#acumulador
soma = 0

for _ in range(10):
    numero = float(input())
    
    if numero > 0:
        #numero é positivo
        #positivos = positivos + 1
        positivos += 1

    soma += numero

print(f"Temos {positivos} numeros positivos.")
print(f"A media dos valores é: {soma/10}")