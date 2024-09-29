# 1. Função básica
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Alice"))  # Olá, Alice!

# 2. Funções com múltiplos parâmetros
def soma(a, b):
    return a + b

print("Soma:", soma(3, 5))  # Soma: 8

# 3. Parâmetros padrão
def potencia(base, expoente=2):
    return base ** expoente

print("Potência:", potencia(3))       # Potência: 9 (3^2)
print("Potência:", potencia(3, 3))    # Potência: 27 (3^3)

# 4. Retornando múltiplos valores
def min_max(lista):
    return min(lista), max(lista)

menor, maior = min_max([10, 20, 5, 40])
print("Menor:", menor, "Maior:", maior)  # Menor: 5 Maior: 40

# 5. Funções aninhadas
def funcao_externa(x):
    def funcao_interna(y):
        return x + y
    return funcao_interna

soma5 = funcao_externa(5) # lembre que a variavel: soma5 esta recebendo tudo que tem dentro de funcao_externa(), logo, pode acessar a: funcao_interna
print("Soma com 5:", soma5(10))  # Soma com 5: 15

# 6. Funções como objetos de primeira classe
def executar(funcao, valor):
    return funcao(valor)

def dobrar(x):
    return x * 2

print("Dobro de 10:", executar(dobrar, 10))  # Dobro de 10: 20

# 7. Funções com argumentos variáveis
def soma_varios(*args):
    return sum(args)

print("Soma de múltiplos argumentos:", soma_varios(1, 2, 3, 4))  # Soma de múltiplos argumentos: 10

# 8. Funções com argumentos nomeados
def mostrar_info(nome, idade, cidade):
    return f"{nome} tem {idade} anos e mora em {cidade}."

print(mostrar_info(idade=30, nome="Carlos", cidade="São Paulo"))  # Carlos tem 30 anos e mora em São Paulo.

# 9. Funções geradoras
def contador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1

print("Contador até 5:")
for numero in contador(5):
    print(numero)  # 0 1 2 3 4

# 10. Decoradores
def decorador(funcao):
    def funcao_decorada():
        print("Antes da execução da função.")
        funcao()
        print("Depois da execução da função.")
    return funcao_decorada

@decorador
def minha_funcao():
    print("Executando minha função.")

minha_funcao()
# Antes da execução da função.
# Executando minha função.
# Depois da execução da função.


"""
Resumo dos Exemplos:

    Função básica: Definindo e chamando uma função simples.
    Múltiplos parâmetros: Usando mais de um argumento.
    Parâmetros padrão: Definindo valores padrão para argumentos.
    Retorno de múltiplos valores: Retornando mais de um valor de uma função.
    Funções aninhadas: Definindo funções dentro de outras funções.
    Funções como objetos de primeira classe: Passando funções como argumentos.
    Argumentos variáveis: Usando *args para múltiplos argumentos.
    Argumentos nomeados: Passando argumentos pelo nome.
    Funções geradoras: Criando geradores com yield.
    Decoradores: Modificando o comportamento de funções usando decoradores.
"""