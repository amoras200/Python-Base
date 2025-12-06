# Tipo de Dado - Para determinar o tipo de dado, você o indica e coloca o comando de entrada em parenteses -

# Int - Inteiro, é o valor numérico sem ponto flutuante. 
n1 = int (input("digite um número: "))
n2 = int (input("digite um número novamente: "))
soma = n1 + n2
sub = n1 - n2
print (f"a soma dos números que você digitou é {soma} e a subtração é {sub}")

# Float - Tipo de dado de ponto flutuante. Valor numérico não inteiro escrito com ponto flutuante (ex: 5.5).
nFloat1 = float(input("digite um número de ponto flutuante: "))
nFloat2 = float(input("digite um número de ponto flutuante qualquer novamente: "))
print(f"A soma dos seus numeros é", nFloat1 + nFloat2)

# String - Isso é uma via de mão dupla, tambem é possivel tornar valores e tipos de dado em strings, assim:
number = 10
str(number) # a saída é texto

print("Eu sou uma String") # Strings - python reconhece como texto aquilo que é colocado entre aspas.

# Para colocar uma palavra entre aspas dentro de uma string, usamos a barra invertida \ Pois sabemos que ela mostra o escape do comando
# Por exemplo:
print("Eu sou uma \"Mensagem\"")
print("I\'m \"Monty Python\"") 
print('Ola "Mundo"')

# Impressão de Várias Linhas - 3 aspas possibilitam varias linhas.
print("""
      Era uma vez
      Os 3 manés
      Eram doidos e malucoes
      Muito manés.
      """)

# Valores Booleanos - verificam a veracidade da coisa - Python é binário e trabalha com apenas dois valores de veracidade, True e False respectivamente 1 e 0.
# Sim isso é verdade; Ou Não, isso é falso. Sempre.
 
# Variáveis - caixas em forma de dados
# o nome da variável deve ser composto de letras maiúsculas ou minúsculas, dígitos e o caractere _ (sublinhado)
# o nome da variável deve começar com uma letra;
# o caractere de sublinhado é uma letra;
# as letras maiúsculas e minúsculas são tratadas como diferentes (um pouco diferente do que no mundo real - Alice e ALICE são os mesmos nomes, mas em Python são dois nomes de variáveis diferentes e, consequentemente, duas variáveis diferentes);
# o nome da variável não deve ser nenhuma das palavras reservadas do Python (as palavras-chave - explicaremos mais sobre isso em breve).

# Palavras reservadas
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
# 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']