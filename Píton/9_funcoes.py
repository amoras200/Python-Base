#Funções
#Para chamar uma função usamos def e então a função.

def minha_funcao():
    print("Essa é minha função") #codigo que será realizado pela função
    #se executado assim, nada acontecerá, é preciso chamar a função.

minha_funcao()
print("------------------------------------")
print("------------------------------------")

idade = 19
def minha_funcao():
    nome = "Gustavo"
    print(f"Essa é  meu nome {nome} e minha idade é {idade}") #codigo que será realizado pela função
    #se executado assim, nada acontecerá, é preciso chamar a função.

minha_funcao()
#print(nome) se isso fosse executado geraria erro, pois a variavel nome não foi definida
#esse é o conceito de variaveis globais e locais.
#Fora da função, essa variavel não existe mais.
#agora este aqui funcionaria, pois ela é global, serve tanto para as funções, quanto para todo o resto.
print(idade)

#é possivel tambem criar funções dentro de funções, e as variaveis das funções pai funcionarao para as ramificações


def somar(numero1,numero2):
    resultado = numero1 + numero2
    print(f"a soma é {resultado}")

somar(4, 8) #aqui eu chamo a função e entrego valores ás variáveis

def saudacao(nome):
    print(f"Ola {nome}")

saudacao("Amorim") #mesma coisa

#e se eu quiser chamar uma variável especifica que está localmente presa a uma função? ultilizamos:
#Return
def somar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

#print(resultado) não funciona pois resultado ainda esta alocado
#o que devemos fazer agora, é chamar a função soma, e ela funcionará assim
#porem, se chamarmos apenas a função soma, ela não printará nada

#print(somar) gera erro pois ele não printa nada, e para isso, jogaremos essa soma á uma nova varável.
resultado_da_soma = somar(5, 8)

print(f"o resultado da soma é {resultado_da_soma}")
