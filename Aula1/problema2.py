# --------------------------------------------------------------------------
# PROBLEMA 2: Cálculo de Média de Notas (Escola)
# --------------------------------------------------------------------------
"""
Cenário: Professor precisa calcular a média final de um aluno
com 4 notas bimestrais.
"""

print("\n📖 PROBLEMA 2: Cálculo de Média Escolar")
print("-" * 50)

# Notas do aluno (pode usar float para notas decimais)
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
nota4 = 9.0

media = (nota1 + nota2 + nota3 + nota4) / 4


situacao = "APROVADO" if media >= 7.0 else "REPROVADO"

print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média final: {media:.1f}")
print(f"Situação: {situacao}")
