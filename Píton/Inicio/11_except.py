# usamos o bloco try .... except para manipular e contornar possiveis erros no cód, por exemplo, suponha que você pede ao usuário que Digite um número inteiro,
# porém ele insere um valor de texto, como uma letra. Isso geraria um erro e travaria o sistema, com except podemos contornar isso.


n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

# r = round(n1 / n2)
# print(f"resultado: {r}")

# o que aconteceria aqui se a variável n2 recebesse o valor 0? Um erro. Pois não é possivel dividir por zero
# para contornar isso, abrimos o bloco try:.....excepet

try:
    r = round(n1 / n2) # a função round arredonda o resultado, colocamos aqui a aplicação que pode gerar erro. tente:
except ZeroDivisionError: # nome do erro que daria
    print(f"não é possivel dividir po zero") # no caso deste erro, o que rodaria para o usuário.
else:   # else para dizer: se não acontecer o erro
    print(f"resultado: {r}")
finally: # finally obriga o codigo á rodar independente de haver ou não erros, mas não é necessário colocar.
    print('fim do calculo')

# caso não saiba o nome do erro, ou apenas queira evitar erros, é possivel adcionar except sem especificar para qual erro.