# Definição de Classe

class MinhaClasse:
    pass

# Construtor

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Métodos

class Carro:
    def ligar(self):
        print("Carro ligado")

# Herança

class Veiculo:
    pass

class Moto(Veiculo):
    pass

# Poiformismo

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

# Encaplulamento

class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

# Métodos Estaticos e Classe