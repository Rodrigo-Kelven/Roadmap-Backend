# Herança de classes
# Exemplo 1:

# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError("Este método deve ser sobrescrito na subclasse.")

# Classe derivada - Cachorro
class Cachorro(Animal):
    def fazer_som(self):
        return "Woof!"

# Classe derivada - Gato
class Gato(Animal):
    def fazer_som(self):
        return "Meow!"

# Classe derivada - Pássaro
class Passaro(Animal):
    def fazer_som(self):
        return "Tweet!"

# Criando instâncias das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Mia")
passaro = Passaro("Lulu")

# Usando métodos das instâncias
print(f"{cachorro.nome} diz: {cachorro.fazer_som()}")  # Rex diz: Woof!
print(f"{gato.nome} diz: {gato.fazer_som()}")          # Mia diz: Meow!
print(f"{passaro.nome} diz: {passaro.fazer_som()}")    # Lulu diz: Tweet!


# Classe derivada com herança múltipla
class AnimalDeEstimacao(Animal):
    def __init__(self, nome, dono):
        super().__init__(nome)
        self.dono = dono

    def info(self):
        return f"{self.nome} é de {self.dono}."

# Classe derivada - Gato de Estimação
class GatoDeEstimacao(Gato, AnimalDeEstimacao):
    def __init__(self, nome, dono):
        Gato.__init__(self, nome)
        AnimalDeEstimacao.__init__(self, nome, dono)

# Criando uma instância da classe GatoDeEstimacao
gato_estimacao = GatoDeEstimacao("Mia", "Alice")
print(gato_estimacao.info())  # Mia é de Alice.
print(f"{gato_estimacao.nome} diz: {gato_estimacao.fazer_som()}")  # Mia diz: Meow!


# Herança múltipla
# Exemplo 1:

class A:
    def metodo_a(self):
        return "Método A"

class B:
    def metodo_b(self):
        return "Método B"

class C(A, B):
    def metodo_c(self):
        return "Método C"

obj = C()
print(obj.metodo_a())  # Método A
print(obj.metodo_b())  # Método B
