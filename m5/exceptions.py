import sys
#erros de compilação / erros de parsing
# if b < 18:
#     pass

#erros em tempo de execução -> Exceções
def fsimples(b):
    a = 1/b

def outrafuncao(a):
    fsimples(a)

#try/except/finally

try:
    a = int(input())
    outrafuncao(a)
    print("Tudo certo")
except ZeroDivisionError:
    print("Não é permitida a divisão por zero")
except ValueError:
    print("Use apenas numeros")
finally:
    print("Sempre apareço")