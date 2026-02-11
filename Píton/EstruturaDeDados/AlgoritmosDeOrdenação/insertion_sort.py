# a ideia do inserton sort é construir uma lista ordenada, um elemento por vez
# pegamos um elemento da lista original e o inserimos na posição correta da lista ordenada
# exemplo: lista = [7,5,1,8,3]
# passo 1: pegamos o primeiro elemento (7) e o colocamos na lista
# lista ordenada = [7]
# passo 2: pegamos o segundo elemento (5) e o inserimos na posição correta na lista ordenada
# lista ordenada = [5,7]
# passo 3: pegamos o terceiro elemento (1) e o inserimos na posição correta na lista ordenada
# lista ordenada = [1,5,7]
# passo 4: pegamos o quarto elemento (8) e o inserimos na posição correta na lista ordenada
# lista ordenada = [1,5,7,8]
# passo 5: pegamos o quinto elemento (3) e o inserimos na posição correta na lista ordenada
# lista ordenada = [1,3,5,7,8]
# implementação do insertion sort em python
def insertion_sort(lista):
    for i in range(1, len(lista)): # começamos do segundo elemento, pois o primeiro já está "ordenado"
        chave = lista[i] # o elemento que queremos inserir na lista ordenada
        j = i - 1 # o índice do último elemento da lista ordenada
        while j >= 0 and chave < lista[j]: # enquanto não chegarmos ao início da lista e o elemento atual for maior que a chave
            lista[j + 1] = lista[j] # deslocamos o elemento para a direita
            j -= 1 # movemos para o próximo elemento da lista ordenada
        lista[j + 1] = chave # inserimos a chave na posição correta
    return lista # retornamos a lista ordenada

print(insertion_sort([7,5,1,8,3]))  # deve retornar [1,3,5,7,8]

# melhor caso: O(n) - quando a lista já está ordenada
# pior caso: O(n^2) - quando a lista está em ordem decrescente
# caso médio: O(n^2)

# quando usar: o insertion sort é mais adequado para listas pequenas ou quase ordenadas, onde sua simplicidade e eficiência podem ser vantajosas
# quando não usar: para listas grandes ou desordenadas, onde algoritmos mais eficientes como quicksort ou mergesort são preferíveis