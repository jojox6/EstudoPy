# =============================================================================
# 📚 TEORIA - PARTE 3: OPERADORES
# =============================================================================

"""
1. OPERADORES ARITMÉTICOS:
   +  : Adição
   -  : Subtração
   *  : Multiplicação
   /  : Divisão (sempre retorna float)
   // : Divisão inteira (arredonda para baixo)
   %  : Módulo (resto da divisão)
   ** : Exponenciação (potência)

2. OPERADORES DE COMPARAÇÃO:
   == : Igual a
   != : Diferente de
   >  : Maior que
   <  : Menor que
   >= : Maior ou igual a
   <= : Menor ou igual a

3. OPERADORES LÓGICOS:
   and : E (ambos devem ser True)
   or  : OU (pelo menos um True)
   not  : NÃO (inverte o valor)
"""

print("\n=== OPERADORES ARITMÉTICOS ===")
a, b = 10, 13
print(f"a = {a}, b = {b}")
print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão Inteira: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponênciação: {a} ** {b} = {a ** b}")

print("\n=== OPERADORES DE COMPARAÇÃO ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} <= {b}: {a <= b}")

print("\n=== OPERADORES LÓGICOS ===")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")
