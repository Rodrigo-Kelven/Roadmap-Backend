# Definindo um método de instância
# Exemplo 1:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

pessoa2 = Pessoa("Bob", 25)
print(pessoa2.apresentar())  # Olá, meu nome é Bob e tenho 25 anos.


# Exemplo 2:

# Definindo uma classe
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinheiro
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    # Método para sacar dinheiro
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")

    # Método para mostrar informações da conta
    def mostrar_informacoes(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

# Criando instâncias da classe ContaBancaria
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob")

# Usando métodos nas instâncias
conta1.mostrar_informacoes()  # Mostra informações da conta de Alice
conta1.depositar(500)          # Deposita na conta de Alice
conta1.sacar(200)              # Saca da conta de Alice

conta2.mostrar_informacoes()  # Mostra informações da conta de Bob
conta2.depositar(300)         # Deposita na conta de Bob
conta2.sacar(400)             # Tenta sacar da conta de Bob
