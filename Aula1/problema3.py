# --------------------------------------------------------------------------
# PROBLEMA 3: Conversor de Temperatura (Celsius ↔ Fahrenheit)
# --------------------------------------------------------------------------
"""
Cenário: Aplicativo de clima precisa converter temperaturas
entre diferentes escalas.

Fórmulas:
- C → F: (C × 9/5) + 32
- F → C: (F - 32) × 5/9
"""

print("\n📖 PROBLEMA 3: Conversor de Temperatura")
print("-" * 50)

# Temperatura em Celsius
temp_celsius = 30

# Conversão para Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32

# Conversão de volta para Celsius (verificação)
temp_celsius_convertido  = (temp_fahrenheit - 32) * 5/9

print(f"{temp_celsius}°C = {temp_fahrenheit:.1f}°F")
print(f"Verificação: {temp_fahrenheit:.1f}°F = {temp_celsius_convertido:.0f}°C")