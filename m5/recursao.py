#f(0) = 1, f(1) = 1
#f(n) = f(n-1) + f(n-2)
# 1 1 2 3 5 8 13 21

#recursividade

def fib(n):
    if n == 0 or n == 1:
        return 1

    resultado = fib(n-1) + fib(n-2)
    return resultado

print(fib(6))