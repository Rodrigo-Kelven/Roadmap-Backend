# 1. List Comprehension básica
quadrados = [x**2 for x in range(10)]
print("Quadrados:", quadrados)  # Quadrados: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. List Comprehension com condição
pares = [x for x in range(10) if x % 2 == 0]
print("Números pares:", pares)  # Números pares: [0, 2, 4, 6, 8]

# 3. Dicionário por Compreensão
dicionario_quadrados = {x: x**2 for x in range(5)}
print("Dicionário de quadrados:", dicionario_quadrados)  # Dicionário de quadrados: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 4. Dicionário por Compreensão com condição
dicionario_pares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Dicionário de pares:", dicionario_pares)  # Dicionário de pares: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 5. Set Comprehension
conjunto = {x**2 for x in range(-5, 6)}
print("Conjunto de quadrados:", conjunto)  # Conjunto de quadrados: {0, 1, 4, 9, 16, 25}

# 6. Set Comprehension com condição
conjunto_pares = {x for x in range(10) if x % 2 == 0}
print("Conjunto de pares:", conjunto_pares)  # Conjunto de pares: {0, 2, 4, 6, 8}

# 7. Compreensão Aninhada
matriz = [[j for j in range(3)] for i in range(3)]
print("Matriz 3x3:", matriz)  # Matriz 3x3: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 8. Compreensão Aninhada com Condição
matriz_pares = [[j for j in range(3) if j % 2 == 0] for i in range(3)]
print("Matriz de pares:", matriz_pares)  # Matriz de pares: [[0], [0], [0]]

# 9. Compreensão com Função
nomes = ['alice', 'bob', 'charlie']
nomes_capitalizados = [nome.capitalize() for nome in nomes]
print("Nomes capitalizados:", nomes_capitalizados)  # Nomes capitalizados: ['Alice', 'Bob', 'Charlie']

# 10. Compreensão com Enumeração
frutas = ['maçã', 'banana', 'laranja']
frutas_indexadas = {i: fruta for i, fruta in enumerate(frutas)}
print("Frutas indexadas:", frutas_indexadas)  # Frutas indexadas: {0: 'maçã', 1: 'banana', 2: 'laranja'}

# 11. Compreensão com zip()
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
dicionario_zip = {num: letra for num, letra in zip(lista1, lista2)}
print("Dicionário com zip:", dicionario_zip)  # Dicionário com zip: {1: 'a', 2: 'b', 3: 'c'}

# 12. Compreensão para Filtrar e Transformar
dados = [1, 2, 3, 4, 5, 6, 7]
dados_transformados = [x * 2 for x in dados if x % 2 == 0]
print("Dados transformados:", dados_transformados)  # Dados transformados: [4, 8, 12]



"""
Resumo dos Exemplos:

    List Comprehension básica: Criação simples de uma lista.
    List Comprehension com condição: Filtrando elementos.
    Dicionário por Compreensão: Criando um dicionário a partir de uma lista.
    Dicionário com condição: Filtrando elementos ao criar um dicionário.
    Set Comprehension: Criando conjuntos a partir de uma expressão.
    Set Comprehension com condição: Filtrando elementos em um conjunto.
    Compreensão Aninhada: Criando listas dentro de listas.
    Compreensão Aninhada com Condição: Filtrando em listas aninhadas.
    Compreensão com Função: Aplicando funções durante a criação da lista.
    Compreensão com Enumeração: Usando índices ao criar dicionários.
    Compreensão com zip(): Combinando listas em dicionários.
    Filtrar e Transformar: Filtrando e transformando dados em uma única expressão.
"""