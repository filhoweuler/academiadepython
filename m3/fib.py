#criar um vetor(lista) de 60 posições com 
# a sequencia Fibonacci

fibonacci = [1, 1]

for _ in range(58):
    novo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_numero)

for numero in fibonacci:
    print(numero)