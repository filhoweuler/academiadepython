#ler o nome da primeira pessoa
primeiro_nome = input("Digite o nome da primeira pessoa: ")
#ler a idade da primeira pessoa
primeira_idade = int(input("Digite a idade da primeira pessoa: "))

#ler o nome da segunda pessoa 
segundo_nome = input("Digite o nome da segunda pessoa: ")
#ler a idade da segunda pessoa
segunda_idade = int(input("Digite a idade da segunda pessoa: "))

#imprimir o nome do mais velho

if primeira_idade > segunda_idade:
    print(primeiro_nome)
else:
    print(segundo_nome)