
#List Comprehension

#Syntatic Sugar - Açucar Sintático

# quadrados = []
# for k in range(1,51):
#     if k % 2 == 0:
#         if k <= 20:
#             quadrados.append(k ** 2)

#versao simplificada
quadrados = [ k ** 2 for k in range(1,51) if k % 2 == 0 if k <= 20 ]
print(quadrados)