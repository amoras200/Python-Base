# Listas/Arrays - para que servem? Listas ajudam á não ter que criar 1 milhão de variaveis. 
frutas = ["banana","maçã","melancia","Uva","Morango","melancia","Uva","melancia","Uva"]
print (frutas)

# se caso queira uma especifica, usamos index - [] que inicia sua contagem da posição 0 - pense em index como a posição das variaveis, sendo a primeira o 0
print(frutas[2]) # printa na tela a fruta melancia, visto que: [0] == banana; [1] == maçã; [2] == melancia

# um intervalo com [:]
print(frutas[2:4]) #sendo o segundo numero a posição literal e assi printará Uva

#é possivel contar a quantidade de vezes que um valor contar
print(frutas.count("Uva"))

#é possivel saber a posição de um valor
print(frutas.index("melancia"))

#a quantidade literal de indexes
print(len(frutas))

#ler e adcionar um valor á lista
nova_fruta = input("Escreva uma fruta: ")
frutas.append(nova_fruta)

#adcionar a lista especificando a posição
nova_fruta = input("Escreva uma fruta: ")
frutas.insert(2, nova_fruta)

#remover item da lista
fruta_removida = frutas
frutas.remove("Uva")

#remover por index
fruta_removida = frutas.pop(3)
print(f"a fruta removida foi {fruta_removida}")

#para copiar uma lista e salvar (como a lista é um objeto, ela necessita deste copy, pois qualquer alteração afetará direamente a variavel)
frutas_copia = frutas.copy
frutas.remove("maçã")
print(frutas)
print(frutas_copia)




#-------------------------------------------
#-------------------------------------------

nomes1 = ["gustavo","guilherme","pablo"]
nomes2 = ["vitor","viviane","veronica"]

nomes3 = nomes1 + nomes2

print(nomes3)

# veja o que acontece ao rodar este programinha
#--------------------------------------------
#--------------------------------------------

#para ordenar
numeros = [4,3,5,1,2,9,8]
numeros.sort()
print(numeros)

#para ordenar na orden reversa
numeros.sort(reverse=True)
print(numeros)