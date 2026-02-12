nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open('input_data.txt', 'w') as f:
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')

# fique atento aos arquivos, um arquivo será criado na pasta do projeto chamado input_data.txt
# com a resposta do usuário.