#ler inteiro do teclado
valor = int(input("Digite o numero: "))

#verificar se esta no intervalo [0,50]
#if valor >= 0 and valor <= 50:
if 0 <= valor <= 50: 
    print("[0,50]")
#verificar intervalo [51, 100]
elif 51 <= valor <= 100:
    print("[51, 100]")
else:
    print("Fora do intervalo")



