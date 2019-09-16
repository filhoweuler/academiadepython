from pilha_poo import Pilha

'''
Dado um arquivo com uma sequencia de {}, () e [], diga se esta
sequencia está balanceada ou não.

Por exemplo: ({}([)]) não está balanceado
             [()({})] está balanceado
             (85){asd}[] está balanceado
'''

# Criar funcao que diz se esta balanceado ou nao

aberturas = ['{', '[', '(']

fechamentos = ['}', ']', ')']

fechamento_abertura = { '}' : '{', ']' : '[', ')' : '(' }

def balanceado(linha):
    '''
    Dada uma string de parenteses, diz se essa string está balanceada
    ou não.
    '''

    pilha = Pilha()

    for c in linha:

        # Caso c seja uma abertura
        if c in aberturas:
            pilha.empilhar(c)

        if c in fechamentos:

            if pilha.vazia():
                return False
            
            if fechamento_abertura[c] != pilha.topo():
                return False
            
            pilha.desempilhar()

    return pilha.vazia()        


# Ler arquivo

arquivo = open('input.dat', 'r')

# Para cada linha no arquivo, dizer se esta balanceado

for linha in arquivo:
    print(linha, end='')
    if balanceado(linha):
        print(" está balanceado")
    else:
        print(" não está balanceado")