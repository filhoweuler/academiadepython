#argumentos ou parametros
#valores passados para uma função

# def f(x,y):
#     return (x+y) ** 2

# a = f(8,2)
# print(a)
# print(f(1,1))

def f():
    global x
    print("Recebi",x)
    #x = x+1
    x += 1
    print("Agora tenho", x)

x = 1
f()
print(x)
