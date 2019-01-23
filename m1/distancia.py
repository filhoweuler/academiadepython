import math

#ler linha com coordenadas no teclado
linha = input()

#separar linha e guardar em duas variaveis
x1 , y1 = linha.split()

#transformar numeros em inteiros
x1 = int(x1)
y1 = int(y1)

linha = input()

x2, y2 = linha.split()

x2 = int(x2)
y2 = int(y2)

#d = raiz( (x1-x2)**2 + (y1-y2)**2 )
distancia = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

print(distancia)