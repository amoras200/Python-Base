# raise serve para forçar um erro, quando python não identifica a posição como um erro, o comando raise é ativado para forçar um erro.
from math import sqrt # apenas para um teste

if __name__ == "__main__": # comumente usado em scripts para testes locais
  try:
    num = int(input("Digite um numero positivo"))
    if num < 0:
      raise ArithmeticError # força a dar esse erro
  except ArithmeticError:
    print(f"O numero fornecido é negativo")
  else:
    print(f"A raiz quadrada é {sqrt(num)}")
  finally:
    print("Fim do calculo")

# ainda era possivel adicionar o comando finally para garantir que mesmo com erro, esse programa rode