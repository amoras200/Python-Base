# a ideia do selection sort é olhar para uma lista de dados,e selecionar o menor valor, e colocar ele na primeira posição
# depois olhar para o restante da lista, selecionar o menor valor e colocar na segunda posição, e assim por diante

# exemplo: lista = [7,5,1,8,3]
# passo 1: olhar para toda a lista, selecionar o menor valor (1) e colocar na primeira posição
# lista = [1,5,7,8,3]
# passo 2: olhar para o restante da lista (5,7,8,3), selecionar o menor valor (3) e colocar na segunda posição
# lista = [1,3,7,8,5]
# passo 3: olhar para o restante da lista (7,8,5), selecionar o menor valor (5) e colocar na terceira posição
# lista = [1,3,5,8,7]
# passo 4: olhar para o restante da lista (8,7), selecionar o menor valor (7) e colocar na quarta posição
# lista = [1,3, 5,7,8]

# implementação do selection sort em python

# linha de racionio: para cada posição da lista, olhar para o restante da lista, selecionar o menor valor e trocar de posição
# precisamos de dois loops, um para percorrer cada posição da lista, e outro para olhar para o restante da lista e armazenar o menor valor

lista = [7,5,1,8,3]

# logica inicial do selection sort: 
# armazeno o tamanho da lista
# para cada posição da lista, assumo que o menor valor está na posição atual
# para o restante da lista, verifico se o valor atual é menor que o menor valor armazenado
# se for, atualizo o indice do menor valor
# após o loop interno, troco o menor valor encontrado com o valor da posição atual

n = len(lista) # armazeno o tamanho da lista
minimo = lista[0] # inicializo o menor valor com o primeiro valor da lista
for i in range(n): # loop para percorrer cada posição da lista
    if lista[i] < minimo: # se o valor atual for menor que o menor valor armazenado
        minimo = lista[i] # atualizo o menor valor
print(f"O menor valor da lista é {minimo}")

# rode o codigo acima para verificar se o menor valor está sendo armazenado corretamente
# encontrar o menor valor funciona, mas ainda não estamos trocando de posição nem reordenando a lista

# encontrar o menor valor é importante, mas o que vale, é encontrar o indice do menor valor, para depois trocar de posição 
# agora vamos implementar o selection sort completo

for i in range(len(lista)): # loop para percorrer cada posição da lista
    menor_indice = i # assumimos que o menor valor está na posição atual
    for j in range(i+1, len(lista)): # loop para olhar para o restante da lista, aqui j representa o indice do valor atual
        if lista[j] < lista[menor_indice]: # se o valor atual for menor que o menor valor armazenado
            menor_indice = j # atualizamos o indice do menor valor
    # após o loop interno, trocamos o menor valor encontrado com o valor da posição atual
    lista[i], lista[menor_indice] = lista[menor_indice], lista[i]


def selection_sorte(lista):
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
                lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

print(selection_sorte([7,5,1,8,3])) # deve retornar [1,3,5,7,8]


# melhor caso: O(n^2) - quando a lista já está ordenada
# pior caso: O(n^2) - quando a lista está em ordem decrescente
# caso médio: O(n^2)


# quando usar: o selection sort é mais adequado para listas pequenas, onde sua simplicidade pode ser vantajosa
# quando não usar: para listas grandes ou desordenadas, onde algoritmos mais eficientes como