# 1. Iterando sobre uma lista
minha_lista = [1, 2, 3, 4, 5]
print("Iterando sobre uma lista:")
for numero in minha_lista:
    print(numero)

# 2. Iterando sobre uma tupla
minha_tupla = (6, 7, 8)
print("\nIterando sobre uma tupla:")
for numero in minha_tupla:
    print(numero)

# 3. Iterando sobre um dicionário
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
print("\nIterando sobre um dicionário (chaves):")
for chave in meu_dicionario:
    print(chave)

print("\nIterando sobre um dicionário (valores):")
for valor in meu_dicionario.values():
    print(valor)

print("\nIterando sobre um dicionário (itens):")
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# 4. Iterando sobre um conjunto
meu_conjunto = {1, 2, 3}
print("\nIterando sobre um conjunto:")
for numero in meu_conjunto:
    print(numero)

# 5. Usando range() para iterar
print("\nUsando range() para iterar:")
for i in range(5):
    print(i)

# 6. Iterando sobre uma string
minha_string = "Python"
print("\nIterando sobre uma string:")
for letra in minha_string:
    print(letra)

# 7. List comprehension - Criando uma nova lista
quadrados = [x**2 for x in range(5)]
print("\nList comprehension para quadrados:", quadrados)

# 8. Dicionário por compreensão
quadrados_dict = {x: x**2 for x in range(5)}
print("\nDicionário por compreensão:", quadrados_dict)

# 9. Usando enumerate() para obter índice e valor
print("\nUsando enumerate() para obter índice e valor:")
for indice, valor in enumerate(minha_lista):
    print(f"Índice {indice}: Valor {valor}")

# 10. Usando zip() para iterar em paralelo
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print("\nUsando zip() para iterar em paralelo:")
for num, letra in zip(lista1, lista2):
    print(f"Número: {num}, Letra: {letra}")

# 11. List Comprehension com condições
numeros = range(10)
quadrados = [x**2 for x in numeros if x % 2 == 0]
print("Quadrados de números pares:", quadrados)

# 12. Dicionário por Compreensão
cubo_dict = {x: x**3 for x in range(5)}
print("Cubos em um dicionário:", cubo_dict)

# 13. Usando zip() para unir duas listas
nomes = ['Alice', 'Bob', 'Charlie']
idades = [24, 30, 22]
pessoas = {nome: idade for nome, idade in zip(nomes, idades)}
print("Dicionário de pessoas:", pessoas)

# 14. Enumerate com List Comprehension
frutas = ['maçã', 'banana', 'laranja']
frutas_indexadas = {i: fruta for i, fruta in enumerate(frutas)}
print("Frutas indexadas:", frutas_indexadas)

# 15. Iteração em listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Elementos da matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
print()

# 16. Usando iteradores com iter() e next()
numeros = [1, 2, 3]
iterador = iter(numeros)
print("Iterando com iteradores:")
for _ in range(len(numeros)):
    print(next(iterador))

# 17. Geradores
def contador(maximo):
    for i in range(maximo):
        yield i

print("Usando geradores:")
for num in contador(5):
    print(num)

# 18. Usando for com unpacking
tuplas = [(1, 'a'), (2, 'b'), (3, 'c')]
print("Unpacking em for:")
for numero, letra in tuplas:
    print(f"Número: {numero}, Letra: {letra}")

# 19. Iterando sobre dicionários com métodos avançados
dicionario = {'a': 1, 'b': 2, 'c': 3}
print("Iterando sobre um dicionário com métodos:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# 20. Comprehension aninhada
resultados = [[i * j for j in range(3)] for i in range(3)]
print("Comprehension aninhada:", resultados)



"""
Resumo do que foi visto:

    Listas, Tuplas, Conjuntos e Dicionários: Estruturas de dados iteráveis.
    range(): Gera uma sequência de números para iteração.
    List Comprehension: Criação de listas de forma concisa.
    zip(): Permite iterar sobre múltiplas coleções simultaneamente || zip(): Combina listas em dicionários.
    Dicionário por Compreensão: Cria dicionários de maneira concisa.
    enumerate(): Cria dicionários com índices || enumerate(): Permite obter o índice e o valor ao mesmo tempo.
    Listas aninhadas: Itera por listas dentro de listas.
    Iteradores: Usa iter() e next() para iteração manual.
    Geradores: Cria um gerador para economizar memória.
    Unpacking: Extrai elementos de tuplas durante a iteração.
    Iteração em dicionários: Usa métodos avançados de dicionários.
    Comprehension aninhada: Cria listas aninhadas de forma concisa.
"""