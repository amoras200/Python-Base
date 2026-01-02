def limpar_texto (texto):
    texto = texto.lower()
    caracteres_especiais = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in caracteres_especiais:
        texto = texto.replace(char, '')
    return texto
def contar_palavras(texto):
    texto_limpo = limpar_texto(texto)
    palavras = texto_limpo.split()
    contador = {}
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador

input_texto = input("Digite um texto: ")
resultado = contar_palavras(input_texto)
print(f"Contagem de palavras: {resultado}")