# Métodos de listas em Python

# 1. append() - Adiciona um elemento ao final da lista
minha_lista = [1, 2, 3]
minha_lista.append(4)
print("append:", minha_lista)  # [1, 2, 3, 4]

# 2. extend() - Adiciona os elementos de um iterável ao final da lista
minha_lista.extend([5, 6])
print("extend:", minha_lista)  # [1, 2, 3, 4, 5, 6]

# 3. insert() - Insere um elemento em uma posição específica
minha_lista.insert(1, 10)
print("insert:", minha_lista)  # [1, 10, 2, 3, 4, 5, 6]

# 4. remove() - Remove o primeiro elemento com o valor especificado
minha_lista.remove(10)
print("remove:", minha_lista)  # [1, 2, 3, 4, 5, 6]

# 5. pop() - Remove e retorna o último elemento da lista (ou o elemento na posição especificada)
ultimo = minha_lista.pop()
print("pop:", ultimo)            # 6
print("após pop:", minha_lista)  # [1, 2, 3, 4, 5]

# 6. clear() - Remove todos os elementos da lista
minha_lista.clear()
print("clear:", minha_lista)     # []

# 7. index() - Retorna o índice do primeiro elemento com o valor especificado
minha_lista = [1, 2, 3, 2, 1]
indice = minha_lista.index(2)
print("index:", indice)          # 1

# 8. count() - Retorna o número de ocorrências de um elemento na lista
contagem = minha_lista.count(2)
print("count:", contagem)        # 2

# 9. sort() - Ordena os elementos da lista
minha_lista.sort()
print("sort:", minha_lista)      # [1, 1, 2, 2, 3]

# 10. reverse() - Inverte a ordem dos elementos na lista
minha_lista.reverse()
print("reverse:", minha_lista)   # [3, 2, 2, 1, 1]

# 11. copy() - Retorna uma cópia rasa da lista
copia_lista = minha_lista.copy()
print("copy:", copia_lista)       # [3, 2, 2, 1, 1]


"""
Resumo dos métodos:

    append(): Adiciona um item ao final da lista.
    extend(): Adiciona elementos de um iterável ao final da lista.
    insert(): Insere um item em uma posição específica.
    remove(): Remove o primeiro item com o valor especificado.
    pop(): Remove e retorna o item na posição especificada (ou o último).
    clear(): Remove todos os itens da lista.
    index(): Retorna o índice do primeiro item com o valor especificado.
    count(): Conta o número de ocorrências de um valor.
    sort(): Ordena os elementos da lista.
    reverse(): Inverte a ordem dos elementos.
    copy(): Retorna uma cópia da lista.
"""