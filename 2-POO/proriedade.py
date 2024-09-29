# Usando propriedades para encapsulamento
# Exemplo 1:

class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def area(self):
        return self.__largura * self.__altura

retangulo = Retangulo(4, 5)
print("Área do retângulo:", retangulo.area)  # Área do retângulo: 20

# Exemplo 2:

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Propriedade para obter o nome
    @property
    def nome(self):
        return self._nome

    # Propriedade para obter e definir o preço
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = novo_preco

    # Método para mostrar informações do produto
    def informacoes(self):
        return f"Produto: {self.nome}, Preço: {self.preco:.2f}"

# Criando uma instância da classe Produto
produto = Produto("Notebook", 2500.00)

# Usando a propriedade
print(produto.informacoes())  # Produto: Notebook, Preço: 2500.00

# Alterando o preço usando a propriedade setter
produto.preco = 2300.00
print(produto.informacoes())  # Produto: Notebook, Preço: 2300.00

# Tentativa de definir um preço negativo
try:
    produto.preco = -100.00
except ValueError as e:
    print(e)  # O preço não pode ser negativo.


"""
Explicação:
    Entenda que as propriedades são 'formas de burlar' ou 'formas de estabeler regras'

    Classe Produto: Tem atributos privados _nome e _preco.
    @property: Usado para definir métodos que podem ser acessados como atributos.
    Setter: Permite que o atributo preco seja atualizado, com validação para evitar preços negativos.
    Uso: O preço é acessado e modificado como se fosse um atributo, mas com lógica adicional por trás.
"""