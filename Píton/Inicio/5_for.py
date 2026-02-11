# For - tambem é uma estrutura de repetição. As vezes é melhor contar quantas vezes o loop aconteceu, 
# do que verdadeiramente o fator que leva ele á acontecer

# imagine, se esse codigo fosse ultilizado:
# i = 0
# while i < 100:
    # faça_algo()
    # i += 1

# imagina ter que contar quantas vezes isso rolou? uma estrutura de repetição é capaz de contar, e no caso, é o For

for i in range(10):
   print("O valor de i é atualmente", i)

# Difetente do java, não é necessario especificar que i somará 1 á ele mesmo. 
# Mas assim como java, o contador se inicia no zero, e portanto o exemplo acima terminará em 9
# range mostra quantas vezes o loop deve ser executado.

# Porém, é possivel sim, especificar aquilo que não foi colocado. 
# Por exemplo:

for i in range(1,11):
   print(i)

# assim iniciará em 1 e irá ate 10.

# iteradores - Range criou um iterador, que é um objeto do python, que permite que criemos uma sequência com ele
# É possivel vizualizar iteradores nas listas, ou strings


# Quando usar? - 
# While é ultilizado quando não se sabe exatamente quantas vezes a sessão irá acontecer
# for é ultilizado quando se tem uma noção

# Break - Quebra o looping

while True:
    numero = int(input("Digite um numero par: "))
    if numero % 2 == 0:
        print("Obrigado!")
        break
    else:
        print("Mano essa é a droga de um numero impar mano")

print("Fim do programa mano")

# Continue - Quando pfoge da condição do if, para ir ao else, o continue faz voltar e pular para o proximo.
# Exemplo com listas 

numeros = [5,3,2,4,8,6,9]
for n in numeros:
    if n % 2 != 0:
        continue
    print(f"o numero {n} é par")