#ler 3 linhas com palavras (strings) do teclado
caracteristica1 = input()
caracteristica2 = input()
caracteristica3 = input()

#tomar decisao baseada nas palavras

if caracteristica1 == "vertebrado":
    #animal vertebrado
    if caracteristica2 == "ave":
        #ave
        if caracteristica3 == "carnivoro":
            #aguia
            print("aguia")
        else:
            print("pomba")
    else:
        #mamifero
        if caracteristica3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    #animal invertebrado
    pass