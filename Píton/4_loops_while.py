#Loops " Enquanto isso acontecer. Faça isso" ;  " Se isso Acontecer, Faça isso. "

# Loops infinitos - Quando algo é ordenado a acontecer enquanto algo imutavel acontece. Por exemplo:


#while True:
#    print("Estou preso dentro de um loop.") # caso vc rode esse programa, ele ficará infinitamente,você terá que encerralo manualmente.

#   outro exemplo

#while 1>0:
#    print("Estou preso dentro de um loop.") # caso vc rode esse programa, ele ficará infinitamente,você terá que encerralo manualmente.
 
# Loops Dependentes - Que dependem de algo para terminar. "Enquanto isso acontecer, faça isso."
# significa que se deixar de acontecer, ele acaba.

# Armazene o maior número atual aqui.
menor_Numero = -999999999
 
# Insira o primeiro valor.
numero = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while numero != -1:
    # O número é maior que o maior_número?
    if numero > menor_Numero:
        # Sim, atualize o maior_número.
        menor_Numero = numero
    # Insira o próximo número.
    numero = int(input("Digite um número ou digite -1 para parar: "))
    # Imprima o maior número.
print("O maior número é:", menor_Numero)

# Counter - É o i para o JAVA, enquanto counter for diferente de um valor, faça isso, e opere em direção ao valor de counter, assim,
# o loop terá um limite. Nesse caso, counter é maior, e vai em direção á o valor zero, de um em um.
counter = 5
while counter != 0: # aqui "counter:" recebe a mesma funcionalidade
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)