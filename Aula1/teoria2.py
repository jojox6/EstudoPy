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
nome = "Joseph"
idade = 30
altura = 1.89
ativo = False

# Verificando tipos de dados
print("\n=== VERIFICANDO TIPOS ===")
print(f"Tipo de {nome}: {type(nome)}")
print(f"Tipo de: {idade}: {type(idade)}")
print(f"Tipo de: {altura}: {type(altura)}")
print(f"Tipo de: {ativo} : {type(ativo)}")