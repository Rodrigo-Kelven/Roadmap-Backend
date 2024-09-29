# Métodos estáticos e de classe
# Exemplo 1:

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @classmethod
    def triplicar(cls, valor):
        return valor * 3

print("Soma:", Matematica.somar(2, 3))  # Soma: 5
print("Triplo de 4:", Matematica.triplicar(4))  # Triplo de 4: 12

# Exemplo 2:
# Este e o melhor exemplo!!
class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def multiplicacao(a, b):
        return a * b

    @staticmethod
    def divisao(a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

# Usando os métodos estáticos
resultado_soma = Matematica.soma(10, 5)
resultado_subtracao = Matematica.subtracao(10, 5)
resultado_multiplicacao = Matematica.multiplicacao(10, 5)
resultado_divisao = Matematica.divisao(10, 5)

print(f"Soma: {resultado_soma}")                # Soma: 15
print(f"Subtração: {resultado_subtracao}")      # Subtração: 5
print(f"Multiplicação: {resultado_multiplicacao}")  # Multiplicação: 50
print(f"Divisão: {resultado_divisao}")          # Divisão: 2.0
