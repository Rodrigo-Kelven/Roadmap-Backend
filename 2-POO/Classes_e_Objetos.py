# 1. Definindo uma classe
# Exemplo 1:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# 2. Criando um objeto
pessoa1 = Pessoa("Alice", 30)
print("Nome:", pessoa1.nome)  # Nome: Alice
print("Idade:", pessoa1.idade)  # Idade: 30

# Exemplo 2:

# Definindo uma classe
class Carro:
    # Construtor da classe
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    # Método para ligar o carro
    def ligar(self):
        self.ligado = True
        print(f"{self.modelo} está ligado.")

    # Método para desligar o carro
    def desligar(self):
        self.ligado = False
        print(f"{self.modelo} está desligado.")

    # Método para mostrar informações do carro
    def info(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Estado: {estado}")

# Criando objetos da classe Carro
carro1 = Carro("Fusca", 1970)
carro2 = Carro("Civic", 2020)

# Usando métodos dos objetos
carro1.info()  # Informações do carro 1
carro1.ligar()  # Liga o carro 1
carro1.info()  # Informações atualizadas do carro 1

carro2.info()  # Informações do carro 2
carro2.ligar()  # Liga o carro 2
carro2.desligar()  # Desliga o carro 2
carro2.info()  # Informações atualizadas do carro 2

# Herança
class Eletrico(Carro):
    def __init__(self, modelo, ano, autonomia):
        super().__init__(modelo, ano)
        self.autonomia = autonomia

    def info(self):
        super().info()
        print(f"Autonomia: {self.autonomia} km")

# Criando um objeto da classe Eletrico
carro_electrico = Eletrico("Tesla Model S", 2021, 500)
carro_electrico.info()  # Informações do carro elétrico
carro_electrico.ligar()  # Liga o carro elétrico
