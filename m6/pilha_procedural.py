pilha = []

def empilhar(_pilha, numero):
    '''
    empilhar (ou push, em inglês) adiciona um elemento no topo da pilha 
    '''
    
    #o final da lista, é o topo da pilha
    _pilha.append(numero)

def desempilhar(_pilha):
    '''
    desempilhar (ou pop, em inglês) retira um elemento do topo da pilha e retorna seu valor
    '''
    val = _pilha[-1]
    del _pilha[-1]
    return val

empilhar(pilha, 10)
empilhar(pilha, 17)
empilhar(pilha, 20)

#pilha[0] = 0

print(pilha)

print(desempilhar(pilha))

print(pilha)