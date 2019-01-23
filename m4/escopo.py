#escopo de uma variavel:
#porção do código onde essa variável é reconhecida
#ou seja, local onde ela existe.

# erro
# def escopo():
#     x = 123
#     print(x)

# escopo()
# print(x)

def funcao():
    global x
    x = 42
    print("Conheco essa variavel?", x)

x = 1
funcao()
print(x)