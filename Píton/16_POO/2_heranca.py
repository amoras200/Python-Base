# Herança em POO, é um dos pilares da Programação Orientada a Objetos.
# Permite criar uma nova classe (classe filha) baseada em uma classe existente (classe mãe).
# A classe filha herda atributos e métodos da classe mãe, podendo adicionar novos ou modificar os
# existentes.
# Exemplo de herança em Python:
class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

    def mostrar_info(self):
        return f"Canal: {self.nome}, Descrição: {self.descricao} Inscritos: {self.inscritos}"
# Classe filha que herda da classe Canal
class CanalDeJogos(Canal): # Veja que a classe CanalDeJogos herda de Canal, como indicado pelos parênteses.
    def __init__(self, nome, descricao, inscritos, jogos_favoritos):
        super().__init__(nome, descricao, inscritos) # Chama o construtor da classe mãe
        self.jogos_favoritos = jogos_favoritos # Novo atributo específico da classe filha

    def mostrar_jogos(self):
        return f"Jogos Favoritos: {', '.join(self.jogos_favoritos)}"
# Criando um objeto da classe filha
canal_jogos = CanalDeJogos("GamerXYZ", "Canal de jogos", 50000, ["Minecraft", "Fortnite", "Valorant"])
print(canal_jogos.mostrar_info()) # Método herdado da classe mãe
print(canal_jogos.mostrar_jogos()) # Método específico da classe filha