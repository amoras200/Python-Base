# Tuplas - diferente das listas, Tuplas são imutaveis.

# Ainda assim, algumas operações podem ser feitas.

cores = ("Azul","Amarelo","Vermelho")

cores_lista = list(cores)

#Coleções - guarda valores de um elemento só
cachorro = {"Nome":"Luma", "Raça":"Shitzu"}
print(cachorro["Nome"])

#Exercicio - Crie uma lista chamada "numeros" contendo os números '1,2,3,4'.
#Realize as seguites operações 
# - Adicione 6 ao fim da lista
# - Remova o número 6 ao final da lista
# - Substitua 4 por 40
# - inverta a ordem dos elementos

num = [1,2,3,4]
num.append(6)
print(num) 

num.remove(4)
num.append(40)
print(num)

num.sort(reverse=True)
print(num)

# Dada a tupla frutas = ("Maçã","Banana","Laranja","Uva"), faça o seguinte:
# - verifique se banana está presente na tupla
# - Converta a tupla em uma lista e adcione abacaxi
# - Converta a lista de volta para uma tupla
fruits = ("Maçã","Banana","Laranja","Uva")

if "Banana" in fruits:
    print("banana está")
else:
    print("banana não está")

#Crie um dicionario chamado aluno com as seguintes informações:
"Nome : Maria" "Idade : 20" " Curso : Engenharia"
#Agora faça as seguintes alterações no dicionário:
#Adicione uma nova chave chamada "nota" com o valor 9.5
#Modifique o valor da chave idade para 21
#Remova curso

#Adicione 3 cursos á chave curso.

aluno = {
    "nome" : "Roberto",
    "idade" : 20,
    "curso" : "Engenharia"
}

aluno["nota"] = 9.5
aluno["idade"] = 21
aluno.pop("cursos")
aluno["curso"] = ["Engenharia","Mátematica","DSM"]

print(aluno["curso"])