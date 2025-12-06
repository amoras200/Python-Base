# Recursão é uma técnica de programação onde uma função 
# chama a si mesma para resolver um problema.

def fatorial(n):
    if n == 0 or n == 1:  # caso base: fatorial de 0 ou 1 é 1
        return 1
    else:
        return n * fatorial(n - 1)  # chamada recursiva

# formula do fatorial: n! = n * (n-1)! 
# caso base é quando n é 0 ou 1
# caso recursivo é quando n > 1, 
# ele chama a si mesmo com n-1 até chegar no caso base.

# resumo da logica:
# fatorial(5) = 5 * fatorial(4)
# fatorial(4) = 4 * fatorial(3)
# fatorial(3) = 3 * fatorial(2)
# fatorial(2) = 2 * fatorial(1)
# fatorial(1) = 1  # caso base
# então, substituindo de volta:
# fatorial(2) = 2 * 1 = 2
# fatorial(3) = 3 * 2 = 6
# fatorial(4) = 4 * 6 = 24
# fatorial(5) = 5 * 24 = 120    

if __name__ == "__main__":
    numero = int(input("Digite um número para calcular o fatorial: "))
    print(f"O fatorial de {numero} é {fatorial(numero)}")

# A recursão é útil para problemas que podem ser divididos em subproblemas menores,
# como cálculo de fatorial, sequência de Fibonacci, busca em árvores, etc.

# No entanto, é importante ter cuidado com a profundidade da recursão,
# pois chamadas recursivas muito profundas podem levar a um estouro de pilha (stack overflow).
# Em Python, o limite padrão de recursão é 1000 chamadas.
# É possível alterar esse limite usando o módulo sys, mas deve-se ter cautela ao fazer isso.
# numeros negativos ou não inteiros não são aceitos na função fatorial acima.   
