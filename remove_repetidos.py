def remove_repetidos(lista):
    lista = sorted(lista)
    listaprov = []
    listaprov.append(lista[0])
    while len(lista) != 0:
        if lista[0] != listaprov[-1]:
            listaprov.append(lista[0])
            del(lista[0])
        else:
            del(lista[0])        
    return listaprov