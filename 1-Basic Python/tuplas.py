# Criando uma tupla de exemplo
tupla = (1, 2, 3, 4, 5)

# 1. count()
contagem = tupla.count(3)  # Conta quantas vezes um elemento aparece na tupla
print(contagem)

# 2. index()
indice = tupla.index(4)  # Retorna o índice da primeira ocorrência de um elemento
print(indice)

# 3. len()
comprimento = len(tupla)  # Retorna o número de elementos na tupla
print(comprimento)

# 4. slicing
fatia = tupla[1:4]  # Obtém uma fatia da tupla
print(fatia)

# 5. membership
existe = 2 in tupla  # Verifica se um elemento está na tupla
print(existe)

# 6. concatenation
tupla2 = (6, 7, 8)
nova_tupla = tupla + tupla2  # Concatena duas tuplas
print(nova_tupla)

# 7. repetition
tupla_repetida = tupla * 2  # Repete a tupla
print(tupla_repetida)

# 8. unpacking
a, b, c, d, e = tupla  # Desempacota os elementos da tupla
print(a, b, c, d, e)

# 9. sorting (com conversão)
tupla_ordenada = tuple(sorted(tupla))  # Ordena os elementos (precisa converter de volta para tupla)
print(tupla_ordenada)

# 10. conversion
lista = list(tupla)  # Converte a tupla em uma lista
print(lista)

# 11. single element tuple
tupla_unica = (1,)  # Tupla com um único elemento (importante a vírgula)
print(tupla_unica)

# 12. nested tuples
tupla_nidificada = (1, (2, 3), 4)  # Tupla contendo outra tupla
print(tupla_nidificada)
