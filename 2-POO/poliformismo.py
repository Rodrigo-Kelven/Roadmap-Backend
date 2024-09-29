# Polimorfismo
# Exemplo 1:

class Ave:
    def fazer_som(self):
        return "Som de ave"

class Pato(Ave):
    def fazer_som(self):
        return "Quack!"

class Canario(Ave):
    def fazer_som(self):
        return "Piu!"

def emitir_som(ave):
    print(ave.fazer_som())

pato = Pato()
canario = Canario()
emitir_som(pato)    # Quack!
emitir_som(canario)  # Piu!

# Exemplo 2:

# Classe base
class Animal:
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

# Função que utiliza polimorfismo
def emitir_sons(animais):
    for animal in animais:
        print(f"{animal.__class__.__name__} diz: {animal.fazer_som()}")

# Criando instâncias de diferentes animais
animais = [
    Cachorro(),
    Gato(),
    Passaro()
]

# Emitindo sons dos animais
emitir_sons(animais)

