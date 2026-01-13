# =============================================================================
# 💻 PRÁTICA - PROBLEMAS REAIS DO DIA-A-DIA
# =============================================================================

print("\n" + "="*70)
print("💻 PROBLEMAS REAIS - EXERCÍCIOS PRÁTICOS")
print("="*70)

# --------------------------------------------------------------------------
# PROBLEMA 1: Calculadora de Gorjeta (Restaurante)
# --------------------------------------------------------------------------
"""
Cenário: Você trabalha em um restaurante e precisa criar um sistema
que calcula a gorjeta do garçom (10%) e o total da conta.
"""

print("\n📖 PROBLEMA 1: Calculadora de Gorjeta")
print("-" * 50)

# Entrada de dados
valor_conta = 150
porcentagem_gorjeta = 10 # 10%

# Cálculos

valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
conta_total = valor_conta + valor_gorjeta 

# Saída Formatada

print(f"O valor da conta R$ {valor_conta:.2f}")
print(f"O valor da gorjeta R$ {valor_gorjeta:.2f}")
print(f"O valor Total R$ {conta_total:.2f}")
