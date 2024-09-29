# Encapsulamento com atributos privados
# Exemplo 1:

"""
Public: qualquer pode ver
Privado: _self.valor | aqui voce vê, mas, como todos programadores são vacinados, isso significa que pela conveção, você não deve mexer!!
Protect: __self.conta | aqui você não ver nem pode acessar! Se tentar acessa-la ou atribuir um valor a ela, será "criada outro valor". Entenda que seiria como criar uma "nova" variavel
"""
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria("Alice")
conta.depositar(100)
print("Saldo:", conta.obter_saldo())  # Saldo: 100


# Exemplo 2:

# Classe com encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor inválido para depósito.")

    # Método para sacar
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor inválido para saque.")

    # Método para mostrar o saldo (acesso ao atributo privado)
    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

# Criando uma instância da classe ContaBancaria
conta = ContaBancaria("Alice", 1000)

# Usando métodos para interagir com a conta
conta.depositar(500)   # Depósito válido
conta.sacar(200)       # Saque válido
conta.mostrar_saldo()   # Mostra saldo atual

# Tentativa de acesso ao atributo privado
# print(conta.__saldo)  # Isso causará um erro, pois __saldo é privado
