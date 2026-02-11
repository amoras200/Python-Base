#Iterando Dicionários

dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for c, v in dados.items():
    print(f"{c}:{v}")

#se caso só valores

dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for v in dados.values():
    print(f"{v}")

#se caso só chaves
dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for c in dados.keys():
    print(f"{c}")