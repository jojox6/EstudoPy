# =============================================================================
# CURSO DE PYTHON - DO BÁSICO AO AVANÇADO
# AULA 1: Fundamentos do Python - Variáveis, Tipos e Operadores
# =============================================================================

"""
🎯 OBJETIVOS DA AULA 1:
- Compreender o que são variáveis e como usá-las
- Aprender os tipos de dados básicos em Python
- Dominar operadores aritméticos, comparação e lógicos
- Resolver problemas reais com conceitos fundamentais
"""

# =============================================================================
# 📚 TEORIA - PARTE 1: VARIÁVEIS
# =============================================================================

"""
VARIÁVEIS são como "caixas" onde guardamos informações na memória do computador.
Cada variável tem um nome e armazena um valor.

Regras para nomear variáveis:
- Deve começar com letra ou _ (nunca número)
- Pode conter letras, números e _
- Não pode usar palavras reservadas (if, for, while, etc.)
- Python é case-sensitive (nome != Nome != NOME)
"""

# Exemplos de variáveis:
nome = "João"  # String (texto)
idade = 25     # Inteiro
altura = 1.75  # Float (decimal)
ativo = True   # Boolean (verdadeiro/falso)

# =============================================================================
# 📚 TEORIA - PARTE 2: TIPOS DE DADOS BÁSICOS
# =============================================================================

"""
TIPOS PRIMITIVOS em Python:

1. int (inteiro): números sem casa decimal
   Ex: 42, -10, 0, 1000

2. float (decimal): números com casa decimal
   Ex: 3.14, -0.5, 2.0

3. str (string): texto entre aspas
   Ex: "Olá", 'Python', "Curso 2025"

4. bool (boolean): apenas True ou False
   Ex: True, False

5. list (lista): coleção ordenada de itens
   Ex: [1, 2, 3, "texto"]

6. dict (dicionário): pares chave-valor
   Ex: {"nome": "Ana", "idade": 30}

7. tuple (tupla): lista imutável
   Ex: (1, 2, 3)

8. None: representa ausência de valor
"""

# Verificando tipos de dados
print("\n=== VERIFICANDO TIPOS ===")
print(f"Tipo de {nome}: {type(nome)}")
print(f"Tipo de {idade}: {type(idade)}")
print(f"Tipo de {altura}: {type(altura)}")
print(f"Tipo de {ativo}: {type(ativo)}")

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
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b:.2f}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponenciação: {a} ** {b} = {a ** b}")

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
que calcula a gorjeta do garçom e o total da conta.
"""

print("\n📖 PROBLEMA 1: Calculadora de Gorjeta")
print("-" * 50)

# Entrada de dados
valor_conta = 150.00
porcentagem_gorjeta = 10  # 10%

# Cálculos
valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
total_pagar = valor_conta + valor_gorjeta

# Saída formatada
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {valor_gorjeta:.2f}")
print(f"TOTAL A PAGAR: R$ {total_pagar:.2f}")

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

# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Situação do aluno
situacao = "APROVADO" if media >= 7.0 else "REPROVADO"

print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média final: {media:.1f}")
print(f"Situação: {situacao}")

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
temp_celsius_convertido = (temp_fahrenheit - 32) * 5/9

print(f"{temp_celsius}°C = {temp_fahrenheit:.1f}°F")
print(f"Verificação: {temp_fahrenheit:.1f}°F = {temp_celsius_convertido:.0f}°C")

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

# Dados do paciente
peso = 70  # kg
altura = 1.75  # metros

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")

# --------------------------------------------------------------------------
# PROBLEMA 5: Calculadora de Desconto (E-commerce)
# --------------------------------------------------------------------------
"""
Cenário: Loja online precisa calcular preço final com desconto
baseado no valor do carrinho.

Regras:
- Até R$ 100: sem desconto
- R$ 100 a R$ 500: 10% de desconto
- R$ 500 a R$ 1000: 15% de desconto
- Acima de R$ 1000: 20% de desconto
"""

print("\n📖 PROBLEMA 5: Calculadora de Desconto")
print("-" * 50)

# Valor do carrinho
valor_carrinho = 750.00

# Calcular desconto
if valor_carrinho < 100:
    desconto_percentual = 0
elif valor_carrinho < 500:
    desconto_percentual = 10
elif valor_carrinho < 1000:
    desconto_percentual = 15
else:
    desconto_percentual = 20

# Cálculos
valor_desconto = valor_carrinho * (desconto_percentual / 100)
valor_final = valor_carrinho - valor_desconto

print(f"Valor original: R$ {valor_carrinho:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"VALOR FINAL: R$ {valor_final:.2f}")

# --------------------------------------------------------------------------
# PROBLEMA 6: Verificador de Senha (Segurança)
# --------------------------------------------------------------------------
"""
Cenário: Sistema precisa validar requisitos mínimos de senha.

Requisitos:
- Mínimo 8 caracteres
- Pelo menos 1 número
- Pelo menos 1 letra maiúscula
"""

print("\n📖 PROBLEMA 6: Verificador de Senha")
print("-" * 50)

senha = "Senha123@"

# Verificações
tamanho_ok = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)
tem_maiuscula = any(char.isupper() for char in senha)

# Validação final
senha_valida = tamanho_ok and tem_numero and tem_maiuscula

print(f"Senha: {'*' * len(senha)}")
print(f"Tamanho mínimo (8): {'✓' if tamanho_ok else '✗'}")
print(f"Contém número: {'✓' if tem_numero else '✗'}")
print(f"Contém maiúscula: {'✓' if tem_maiuscula else '✗'}")
print(f"Status: {'VÁLIDA' if senha_valida else 'INVÁLIDA'}")

# --------------------------------------------------------------------------
# PROBLEMA 7: Cálculo de Horas Trabalhadas (Folha de Pagamento)
# --------------------------------------------------------------------------
"""
Cenário: RH precisa calcular horas extras de funcionários.

Regras:
- Jornada normal: 8 horas/dia
- Hora extra: 50% a mais sobre o valor da hora normal
"""

print("\n📖 PROBLEMA 7: Cálculo de Horas Extras")
print("-" * 50)

# Dados do funcionário
horas_trabalhadas = 10  # horas no dia
salario_mensal = 3000.00  # salário base
dias_uteis = 22  # dias úteis no mês

# Cálculo do valor da hora normal
horas_normais_mes = 8 * dias_uteis
valor_hora_normal = salario_mensal / horas_normais_mes

# Cálculo das horas extras
horas_extra = max(0, horas_trabalhadas - 8)
valor_hora_extra = valor_hora_normal * 1.5  # 50% a mais

# Total do dia
valor_total_dia = (8 * valor_hora_normal) + (horas_extra * valor_hora_extra)

print(f"Horas trabalhadas: {horas_trabalhadas}h")
print(f"Horas normais: 8h")
print(f"Horas extras: {horas_extra}h")
print(f"Valor hora normal: R$ {valor_hora_normal:.2f}")
print(f"Valor hora extra: R$ {valor_hora_extra:.2f}")
print(f"Total do dia: R$ {valor_total_dia:.2f}")

# --------------------------------------------------------------------------
# PROBLEMA 8: Calculadora de Parcelas (Financiamento)
# --------------------------------------------------------------------------
"""
Cenário: Loja precisa calcular valor de parcelas de um financiamento.

Fórmula: Valor da parcela = Valor total / Número de parcelas
"""

print("\n📖 PROBLEMA 8: Calculadora de Parcelas")
print("-" * 50)

valor_produto = 1200.00
num_parcelas = 12
valor_parcela = valor_produto / num_parcelas

print(f"Valor do produto: R$ {valor_produto:.2f}")
print(f"Número de parcelas: {num_parcelas}x")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
print(f"Total pago: R$ {valor_parcela * num_parcelas:.2f}")

# =============================================================================
# 🎯 EXERCÍCIOS PROPOSTOS
# =============================================================================

print("\n" + "="*70)
print("🎯 EXERCÍCIOS PARA PRATICAR")
print("="*70)

print("""
1. Crie um programa que calcule a área de um retângulo
   (base × altura) com valores fornecidos pelo usuário.

2. Faça um conversor de km/h para m/s (divida por 3.6).

3. Crie um sistema que verifica se uma pessoa pode votar
   (idade ≥ 16 no Brasil).

4. Calcule o valor final de um produto com imposto
   (imposto de X% sobre o valor original).

5. Crie um programa que calcula quanto você vai gastar
   de combustível em uma viagem (distância / consumo).

💡 DICA: Modifique os valores dos problemas acima e veja
   os resultados mudarem! A melhor forma de aprender é
   praticando!
""")

# =============================================================================
# 📝 RESUMO DA AULA 1
# =============================================================================

print("\n" + "="*70)
print("📝 RESUMO - AULA 1: Fundamentos do Python")
print("="*70)

print("""
✅ VOCÊ APRENDEU:
   ✓ Variáveis e como armazenar dados
   ✓ Tipos de dados básicos (int, float, str, bool)
   ✓ Operadores aritméticos, comparação e lógicos
   ✓ Conversão entre tipos (casting)
   ✓ Resolver problemas reais com Python

📌 PRÓXIMA AULA (Aula 2):
   - Estruturas de decisão (if/elif/else)
   - Estruturas de repetição (for/while)
   - Listas e suas operações
   - Mais problemas práticos!

💪 DESAFIO:
   Tente refazer os Problemas 1-8 alterando os valores
   e adicionando novas funcionalidades!
""")

print("\n" + "="*70)
print("🎉 FIM DA AULA 1! Continue praticando!")
print("="*70)
