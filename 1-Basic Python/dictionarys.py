# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

# 1. keys()
print(dicionario.keys())  # Retorna uma visão das chaves do dicionário

# 2. values()
print(dicionario.values())  # Retorna uma visão dos valores do dicionário

# 3. items()
print(dicionario.items())  # Retorna uma visão dos pares (chave, valor)

# 4. get()
print(dicionario.get("nome"))  # Retorna o valor associado à chave

# 5. pop()
idade = dicionario.pop("idade")  # Remove a chave e retorna seu valor
print(idade)
print(dicionario)

# 6. popitem()
ultimo_item = dicionario.popitem()  # Remove e retorna o último par (chave, valor)
print(ultimo_item)
print(dicionario)

# 7. update()
dicionario.update({"profissao": "Engenheira"})  # Adiciona ou atualiza pares (chave, valor)
print(dicionario)

# 8. setdefault()
cidade = dicionario.setdefault("cidade", "Rio de Janeiro")  # Retorna o valor se a chave existir, caso contrário, define e retorna o valor padrão
print(cidade)
print(dicionario)

# 9. clear()
dicionario.clear()  # Remove todos os itens do dicionário
print(dicionario)  # Deve imprimir um dicionário vazio

# 10. copy()
dicionario = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}
dicionario_copia = dicionario.copy()  # Cria uma cópia do dicionário
print(dicionario_copia)

# 11. fromkeys()
novos_dados = dict.fromkeys(["nome", "idade", "cidade"], "Desconhecido")  # Cria um novo dicionário com chaves específicas
print(novos_dados)

# 12. __contains__()
print("nome" in dicionario)  # Verifica se a chave existe no dicionário

# 13. len()
print(len(dicionario))  # Retorna o número de pares (chave, valor) no dicionário

# 14. del
del dicionario["cidade"]  # Remove a chave "cidade"
print(dicionario)

# 15. comprehension
dicionario = {k: v for k, v in zip(["nome", "idade", "cidade"], ["Alice", 30, "São Paulo"])}  # Cria um dicionário usando compreensão
print(dicionario)

# 16. Criando um dicionário
dicionario = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'São Paulo'
}
print("Dicionário inicial:", dicionario)

# 17. Acessando valores
print("Nome:", dicionario['nome'])  # Nome: Alice

# 18. Modificando valores
dicionario['idade'] = 31
print("Idade modificada:", dicionario['idade'])  # Idade modificada: 31

# 19. Adicionando novos pares chave-valor
dicionario['profissão'] = 'Engenheira'
print("Dicionário após adição:", dicionario)

# 20. Removendo um item com `del`
del dicionario['cidade']
print("Dicionário após remoção de 'cidade':", dicionario)

# 21. Usando `pop()` para remover e retornar um item
profissao = dicionario.pop('profissão')
print("Profissão removida:", profissao)  # Profissão removida: Engenheira
print("Dicionário após pop:", dicionario)

# 22. Usando `get()` para acessar valores
idade = dicionario.get('idade', 'Não encontrado')
print("Idade com get():", idade)  # Idade com get(): 31

# 23. Verificando se uma chave existe
if 'nome' in dicionario:
    print("A chave 'nome' existe no dicionário.")

# 24. Iterando sobre chaves e valores
print("Iterando sobre chaves e valores:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# 24. Usando `keys()` e `values()`
chaves = dicionario.keys()
valores = dicionario.values()
print("Chaves:", list(chaves))  # Chaves: ['nome', 'idade']
print("Valores:", list(valores))  # Valores: ['Alice', 31]

# 25. Criando um dicionário a partir de uma lista de tuplas
lista_tuplas = [('a', 1), ('b', 2), ('c', 3)]
dicionario_de_tuplas = dict(lista_tuplas)
print("Dicionário a partir de tuplas:", dicionario_de_tuplas)

# 26. Usando `setdefault()`
dicionario.setdefault('pais', 'Brasil')
print("Dicionário após setdefault:", dicionario)

# 27. Mesclando dicionários com `update()`
novo_dicionario = {'idade': 32, 'pais': 'Brasil'}
dicionario.update(novo_dicionario)
print("Dicionário após update:", dicionario)

# 28. Compreensão de dicionário
dicionario_comprensao = {x: x**2 for x in range(5)}
print("Dicionário por compreensão:", dicionario_comprensao)

# 29. Ordenando um dicionário por chaves
dicionario_ordenado = dict(sorted(dicionario_comprensao.items()))
print("Dicionário ordenado por chaves:", dicionario_ordenado)

# 30. Filtrando um dicionário
dicionario_filtrado = {k: v for k, v in dicionario_ordenado.items() if v > 5}
print("Dicionário filtrado:", dicionario_filtrado)

# 31. Clonando um dicionário
dicionario_clone = dicionario.copy()
print("Cópia do dicionário:", dicionario_clone)

# 32. Usando `defaultdict` do módulo `collections`
from collections import defaultdict

dicionario_default = defaultdict(int)
dicionario_default['a'] += 1
dicionario_default['b'] += 2
print("Dicionário com defaultdict:", dict(dicionario_default))


"""
Resumo dos Exemplos:

    Criando um dicionário: Inicialização básica.
    Acessando valores: Usando a chave para obter um valor.
    Modificando valores: Atualizando um valor existente.
    Adicionando novos pares chave-valor: Adicionando elementos ao dicionário.
    Removendo um item com del: Excluindo um item.
    Usando pop(): Removendo e retornando um item.
    Usando get(): Acessando valores com um valor padrão.
    Verificando se uma chave existe: Usando in para checar a existência.
    Iterando sobre chaves e valores: Usando items() para percorrer.
    Usando keys() e values(): Obtendo chaves e valores como listas.
    Criando um dicionário a partir de tuplas: Inicializando com uma lista de tuplas.
    Usando setdefault(): Definindo um valor padrão se a chave não existir.
    Mesclando dicionários com update(): Unindo dois dicionários.
    Compreensão de dicionário: Criando dicionários de maneira concisa.
    Ordenando um dicionário: Usando sorted() para ordenar por chaves.
    Filtrando um dicionário: Criando um novo dicionário com base em condições.
    Clonando um dicionário: Usando copy() para duplicar.
    Usando defaultdict: Criando dicionários com valores padrão.
"""