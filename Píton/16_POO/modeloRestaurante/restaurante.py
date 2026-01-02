class Restaurante:
   nome = ''
   categoria = ''
   ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"


restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurante_praca), '\n')
print(vars(restaurante_praca), '\n')

print(restaurante_praca.nome)

def verificar_atividade(restaurante):
    if restaurante.ativo:
        print("O restaurante está ativo...")
    else:
        print("O restaurante não esta ativo...")

print(verificar_atividade(restaurante_praca))
