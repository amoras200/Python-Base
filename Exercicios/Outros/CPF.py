
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf[:10], range(11, 1, -1))

    return cpf[-2:] == primeiro_digito + segundo_digito
CPF = input("Digite o CPF (somente números): ")
print(validar_cpf(CPF))