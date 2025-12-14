# ulilie selection sort para ordenar uma lista de Stings em ordem alfabética.
def selection_sorte(lista):
    n = len(lista)
    for i in range(n-1):
        menor_indice = i
        for j in range(i+1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

listas_de_strings = ["banana", "abacaxi", "laranja", "uva", "manga"]
print(selection_sorte(listas_de_strings))  # deve retornar ['abacaxi','banana', 'laranja', 'manga', 'uva']
