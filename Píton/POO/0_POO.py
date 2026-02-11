# POO em python: Programação Orientada a Objetos

# conceitos básicos de POO: classe, objeto, atributo, método, encapsulamento, herança, polimorfismo
# exemplo simples de classe e objeto em python

class Pessoa:
    def __init__(self,altura, peso, nome, idade):
        self.altura = altura #atributo
        self.peso = peso #atributo
        self.nome = nome #atributo
        self.idade = idade #atributo
    
    def saudar(self): # método
        return print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos, peso {self.peso} com {self.altura}m de altura.")
    
# criando um objeto da classe Pessoa
pessoa1 = Pessoa(1.79, 75 , "Amorim", 19)

print(pessoa1.saudar()) # chamando o método apresentar