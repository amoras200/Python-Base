# retirado de: https://www.beecrowd.com.br/judge/pt/problems

"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

Exemplos de Entrada	Exemplos de Saída
12 1 5.30
16 2 5.10

VALOR A PAGAR: R$ 15.50
"""


# Resolva:


















print("Exemplo de solução:")
# Solução:


dados1 = input().split()
codigoPeca1 = int(dados1[0])
qtdPeca1 = int(dados1[1])
valorPeca1 = float(dados1[2])

dados2 = input().split()
codigoPeca2 = int(dados2[0])
qtdPeca2 = int(dados2[1])
valorPeca2 = float(dados2[2])

valorPagar = (qtdPeca1 * valorPeca1) + (qtdPeca2 * valorPeca2)
print(f"VALOR A PAGAR: R$ {valorPagar:.2f}")

