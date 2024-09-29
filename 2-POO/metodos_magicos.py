# Métodos mágicos
# Exemplo 1:

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = p1 + p2
print("Ponto resultante:", (p3.x, p3.y))  # Ponto resultante: (4, 6)


# Exemplo 2:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)
print(pessoa)  # Saída: Alice, 30 anos

# Exemplo 3:

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return f"Carro(modelo='{self.modelo}', ano={self.ano})"

# Criando uma instância da classe Carro
carro = Carro("Fusca", 1970)
print(repr(carro))  # Saída: Carro(modelo='Fusca', ano=1970)

# Exemplo 4:

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, other):
        return self.preco == other.preco

    def __lt__(self, other):
        return self.preco < other.preco

# Criando instâncias da classe Produto
produto1 = Produto("Notebook", 2500)
produto2 = Produto("Smartphone", 2000)
produto3 = Produto("Tablet", 2500)

print(produto1 == produto2)  # Saída: False
print(produto1 == produto3)  # Saída: True
print(produto1 < produto2)    # Saída: False

# Exemplo 5:

class ListaPersonalizada:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def __len__(self):
        return len(self.itens)

# Criando uma instância da classe ListaPersonalizada
lista = ListaPersonalizada()
lista.adicionar(1)
lista.adicionar(2)

print(len(lista))  # Saída: 2


"""
Resumo

Esses exemplos mostram como usar métodos mágicos em Python para:

    Inicialização de objetos (__init__)
    Representação em string (__str__ e __repr__)
    Comparação de objetos (__eq__, __lt__)
    Cálculo do comprimento (__len__)

    Operacoes Mtematicas:
        Adição(+): __add__(self, other)
        Subtração(-): __sub__(self, other)
        Multiplicação(*): __mul__(self, other) 
        Divisão(/): __truediv__(self, other)
        Divisão inteira(//):  __floordiv__(self, other)
        Módulo(%): __mod__(self, other)
        Potência(**): __pow__(self, other)

    Métodos de Comparação:
        Igualdade (==): __eq__(self, other)
        Desigualdade (!=): __ne__(self, other)
        Menor que (<): __lt__(self, other)
        Menor ou igual a (<=): __le__(self, other)
        Maior que (>): __gt__(self, other) 
        Maior ou igual a (>=): __ge__(self, other)

"""