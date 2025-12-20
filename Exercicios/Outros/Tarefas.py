
tarefas = ["Comer","Correr","Estudar","Cantar","Visitar a vó"]

x = 3
while x == 3: 
    x = input("""Gostaria de adcionar uma tarefa? ou marcar a próxima como conclúida? 
          Selecione:[1] adcionar tarefa
                    [2] marcar como concluída
                    [3] sair
          Resposta: """)
    if (x == "1"):
        nova_Tarefa = input("Qual tarefa você gostaria de adcionar? ")
        tarefas.append(nova_Tarefa)
        print(tarefas)
    elif ( x == "2"):
        tarefas.pop()
        print(tarefas)
    elif x == 3:
        break
print(f"Suas tarefas são: {tarefas} , Obrigado!")
    