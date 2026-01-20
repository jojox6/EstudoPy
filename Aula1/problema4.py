# --------------------------------------------------------------------------
# PROBLEMA 4: Calculadora de IMC (Índice de Massa Corporal)
# --------------------------------------------------------------------------
"""
Cenário: Nutricionista precisa calcular o IMC de pacientes.

IMC = peso (kg) / altura² (m)

Classificação:
- Abaixo do peso: IMC < 18.5
- Peso normal: 18.5 ≤ IMC < 25
- Sobrepeso: 25 ≤ IMC < 30
- Obesidade: IMC ≥ 30
"""

print("\n📖 PROBLEMA 4: Calculadora de IMC")
print("-" * 50)

# Temperatura em Celsius
entrada =  input("Digite o seu peso: ")
peso = float(entrada)

entrada2 = input("Digite sua altura: ")
altura = float(entrada2)

imc = (peso / altura **2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif  imc < 25:
    classificacao = "Peso Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")