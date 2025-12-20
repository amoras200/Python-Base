# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
numeros_impares = 0
numeros_pares = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        numeros_impares += 1
    else:
        # Aumente o contador even_numbers.
        numeros_pares += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
    
# Imprimir resultados.
print("Números ímpares contam:", numeros_impares)
print("Números pares contam:", numeros_pares)