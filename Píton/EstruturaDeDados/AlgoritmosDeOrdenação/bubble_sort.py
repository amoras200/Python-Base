# o bubble sort funciona comparando elementos adjacentes e trocando-os de posição se estiverem na ordem errada
# esse processo é repetido até que a lista esteja ordenada
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range( n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
print(bubble_sort([7,5,1,8,3]))  # deve retornar [1,3,5,7,8]

# melhor caso: O(n) - quando a lista já está ordenada
# pior caso: O(n^2) - quando a lista está em ordem decrescente
# caso médio: O(n^2) - quando a lista está em ordem aleatória

# esse O antes de (n) significa ordem de complexidade, ou seja, como o tempo de execução do algoritmo cresce em relação ao tamanho da entrada (n)
# no melhor caso, o algoritmo precisa apenas de uma passagem pela lista para verificar que ela já está ordenada, resultando em uma complexidade linear O(n)
# no pior caso, o algoritmo precisa fazer várias passagens pela lista, trocando elementos em cada passagem, resultando em uma complexidade quadrática O(n^2)
# no caso médio, o algoritmo também tende a ter uma complexidade quadrática O(n^2), pois em média, ele precisará fazer várias pass

# quando usar: o bubble sort é mais adequado para listas pequenas ou quase ordenadas, onde sua simplicidade e facilidade de implementação podem ser vantajosasagens
# quando não usar: para listas grandes ou desordenadas, onde algoritmos mais eficientes