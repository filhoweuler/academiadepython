
#dicionarios



#conjunto de chaves/valor


# - cada chave é unica
# - uma chave pode ser de varios tipos (int, float, string, tupla...)
# - nao é uma lista de valores
# - sempre procurar por chaves, nunca valores







traducoes = {  
    'gato':'cat',
    'cachorro':'dog',
    'mesa':'table',
}

numeros = { 'one': 1, 'two': 2 , 'three': 3 }

print(traducoes)
print(numeros)




#acessar elementos




#checar se um elemento esta no dicionario




#acessar os elementos de um dicionario com for

#keys()
for chave in traducoes.keys():
    print(chave,"->",traducoes[chave])

#items()
for (chave, valor) in traducoes.items():
    print(chave,"->",valor)

#values()
for palavra in traducoes.values():
    print(palavra)


#dicionarios sao mutáveis!!!


#adicionar ou modificar é simples
traducoes['copo'] = 'glass'
traducoes['gato'] = 'kitten'

for chave in traducoes.keys():
    print(chave,"->",traducoes[chave])


#remover elementos

del traducoes['gato']

print(traducoes)

del traducoes['gato']