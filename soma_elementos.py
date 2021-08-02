def soma_elementos(lista):
    x = len(lista) - 1
    y = 0
    soma = 0
    if len(lista) == 3:
        soma = lista[0] + lista[1] + lista[2]
        return soma
    else:
        if len(lista) % 2 == 0:
            while x > y:
                soma = soma + (lista[y] + lista[x])
                y = y + 1
                x = x - 1
        else:
            while x > y:
                soma = soma + (lista[y] + lista[x])
                y = y + 1
                x = x - 1
            soma = soma + lista[-1]
         
    return soma
