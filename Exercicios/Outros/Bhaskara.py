import cmath

def calcular_bhaskara(a, b, c):
  """
  Calcula as raízes de uma equação de segundo grau (ax² + bx + c = 0) usando a fórmula de Bhaskara.

  Args:
    a (float): O coeficiente 'a'.
    b (float): O coeficiente 'b'.
    c (float): O coeficiente 'c'.

  Returns:
    Uma tupla contendo as raízes da equação.
    Retorna uma mensagem de erro se o coeficiente 'a' for zero.
  """
  if a == 0:
    return "O coeficiente 'a' não pode ser zero para uma equação de segundo grau."

  # Calcula o delta (discriminante)
  delta = (b**2) - 4 * a * c

  # Verifica o valor do delta para determinar o tipo de raízes
  if delta > 0:
    # Duas raízes reais e diferentes
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    return f"As raízes da equação são: x1 = {x1} e x2 = {x2}"
  elif delta == 0:
    # Uma única raiz real
    x = -b / (2 * a)
    return f"A equação possui uma única raiz real: x = {x}"
  else:
    # Duas raízes complexas
    # Usamos o módulo 'cmath' para lidar com números complexos
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return f"A equação possui duas raízes complexas: x1 = {x1} e x2 = {x2}"

# --- Exemplos de uso da função ---

# Exemplo 1: Duas raízes reais
print("Exemplo 1: Duas raízes reais (x² - 5x + 6 = 0)")
print(calcular_bhaskara(1, -5, 6))
# Esperado: As raízes da equação são: x1 = 3.0 e x2 = 2.0
print("-" * 30)

# Exemplo 2: Uma raiz real
print("Exemplo 2: Uma única raiz real (x² + 4x + 4 = 0)")
print(calcular_bhaskara(1, 4, 4))
# Esperado: A equação possui uma única raiz real: x = -2.0
print("-" * 30)

# Exemplo 3: Raízes complexas
print("Exemplo 3: Raízes complexas (x² + 2x + 5 = 0)")
print(calcular_bhaskara(1, 2, 5))
# Esperado: A equação possui duas raízes complexas: x1 = (-1+2j) e x2 = (-1-2j)
print("-" * 30)

# Exemplo 4: Coeficiente 'a' igual a zero
print("Exemplo 4: Coeficiente 'a' igual a zero (0x² + 3x - 9 = 0)")
print(calcular_bhaskara(0, 3, -9))
# Esperado: O coeficiente 'a' não pode ser zero para uma equação de segundo grau.