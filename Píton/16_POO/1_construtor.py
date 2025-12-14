# O metodo construtor em Python é definido pelo metodo especial __init__. Ele é automaticamente chamado quando um novo objeto da classe é criado.
# Criar um construtor permite inicializar os atributos do objeto com valores específicos no momento da criação do objeto.
# Ainda que não seja obrigatório definir um construtor, é uma prática comum e recomendada para garantir que os objetos sejam criados com um estado inicial válido.

class Animal:
    def __init__(self, especie, idade): # Este é o construtor, que inicializa os atributos do objeto, ele é chamado automaticamente quando um novo objeto é criado.
        self.especie = especie  # Atributo
        self.idade = idade      # Atributo
        print(f"Um novo animal foi criado: {self.especie}, {self.idade} anos.")

# Criando objetos da classe Animal
animal1 = Animal("cachorro", 3) # O construtor é chamado aqui, rode o programa para ver a mensagem de criação do animal.
animal2 = Animal("gato", 2)

# Outros metodos podem ser definidos na classe para manipular os atributos ou realizar ações relacionadas ao objeto. Porem, elas tem que ser chamadas, 
# diferente do construtor que é chamado automaticamente.

# esses metodos geralmente são definidos dentro da classe, mas podem ser definidos fora.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        print(f"Carro criado: {self.marca} {self.modelo}, Ano: {self.ano}")
    def som(self, som):
        print(f"O carro {self.marca} {self.modelo} faz: {som}")

# Criando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
# Chamando o metodo som para os objetos carro1 e carro2
carro1.som("Vrum Vrum")
carro2.som("Broom Broom")