def imprime_hello_world():
    print("Hello World")

def executa_calculo_magico(numero):
    resultado = 7 * 4 + 5 * (12 + numero) / 3*numero + numero ** 2
    return resultado

a = 4
res = executa_calculo_magico(a)
print(res)

nome = input()
