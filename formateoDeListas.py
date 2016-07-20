lista = ['a','b','c','h']

def transList(listaNew):
    lista.sort()
    listaFin = []
    lenLista = len(lista) - 1
    loop = 0

    while loop <= lenLista:
        itemList = 0
        lista2 = []
        while itemList <= loop:
            lista2.append(lista[itemList])
            itemList = itemList + 1
        listaFin.append(lista2)
        loop = loop + 1
    print listaFin


transList(lista)
# Salida: [['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'h']]
