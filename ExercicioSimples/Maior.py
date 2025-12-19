"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

maiorAB = (a + b + abs(a - b)) // 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada
7 14 106
Exemplos de Saída
106 eh o maior
"""


entrada = input().split()
n1,n2,n3 = int(entrada[0]), int(entrada[1]), int(entrada[2])
maiorAB = (n1 + n2 + abs(n1 - n2)) / 2
maiorABC = (maiorAB + n3 + abs(maiorAB - n3)) / 2
print(f"{maiorABC:.0f} eh o maior")