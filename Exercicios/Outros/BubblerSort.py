# Implemente o algorito Bubble Sort em Python para ordenar ua lista de números em ordem crescente.
print("lista antes da ordenação: [7,5,1,8,3]")
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range( n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("lista ordenada: ",bubble_sort([7,5,1,8,3]))  # deve retornar [1,3,5,7,8]

# agora em ordem decrescente

def bubble_sort_desc(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range( n - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("lista ordenada decrescentemente: ", bubble_sort_desc([7,5,1,8,3]))  # deve retornar [8,7,5,3,1]
