# =============================================================================
# 📚 TEORIA - PARTE 4: CONVERSÃO DE TIPOS (CASTING)
# =============================================================================

"""
Às vezes precisamos converter um tipo em outro:

- int(): converte para inteiro
- float(): converte para decimal
- str(): converte para string/texto
- bool(): converte para boolean

⚠️ Cuidado: nem todas conversões são possíveis!
"""
print("\n=== CONVERSÃO DE TIPOS ===")
numero_texto = "42"
numero_int = int(numero_texto)
print(f"String '{numero_texto}' → Int {numero_int}")

decimal = 3.9
inteiro = int(decimal)  # Trunca (não arredonda!)
print(f"Float {decimal} → Int {inteiro}")

numero = 100
texto = str(numero)
print(f"Int {numero} → String '{texto}'")

# Conversões booleanas
print(f"\nbool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('texto'): {bool('texto')}")