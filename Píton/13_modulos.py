# modulos sãõ umaespecie de biblioteac, com metodos, funções e constantes prontas para serem usadas.
# para usar um modulo, usamos a palavra reservada import seguida do nome do modulo.

import math  # importando o modulo math (matematica)

num = 64
print("a raiz de 64 é: ",math.sqrt(num))  # usando a função sqrt (raiz quadrada) do modulo math

# É possivel importar apenas uma função específica de um modulo usando a palavra reservada from seguida do nome do modulo, a palavra import e o nome da função.

from random import randint  # importando apenas a função randint do modulo random

print("numero sorteado: ",randint(1, 10))  # usando a função randint (número inteiro aleatório) do modulo random

# também é possivel importar todas as funções de um modulo usando o asterisco * após a palavra import.
from datetime import *  # importando todas as funções do modulo datetime
print("data: ", date.today())  # usando a função today (data atual) do modulo datetime
print("data e hora: ", datetime.now())  # usando a função now (data e hora atual) do modulo datetime

# também é possivel criar apelidos para modulos ou funções usando a palavra reservada as.
import math as m  # importando o modulo math com o apelido m
print("5 fatorial é: ", m.factorial(5))  # usando a função factorial (fatorial) do modulo math com o apelido m
