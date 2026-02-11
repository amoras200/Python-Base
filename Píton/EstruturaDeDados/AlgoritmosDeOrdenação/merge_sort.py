# a ideia do merge sort é dividir a lista em duas metades, ordenar cada metade recursivamente e depois mesclar as duas metades ordenadas
# dividir para conquistar
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

print(merge_sort([7,5,1,8,3]))  # deve retornar [1,3,5,7,8]

# melhor caso: O(n log n) - quando a lista já está ordenada
# pior caso: O(n log n) - quando a lista está em ordem decrescente
# caso médio: O(n log n)

# quando usar: o merge sort é adequado para listas grandes e quando a estabilidade da ordenação é importante
# quando não usar: para listas pequenas, onde algoritmos mais simples como insertion sort podem ser mais