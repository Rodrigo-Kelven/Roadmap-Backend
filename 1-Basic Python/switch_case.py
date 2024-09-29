# 1. Usando if, elif e else
opcao = 2
if opcao == 1:
    print("Você escolheu a opção 1.")
elif opcao == 2:
    print("Você escolheu a opção 2.")
elif opcao == 3:
    print("Você escolheu a opção 3.")
else:
    print("Opção inválida.")

# 2. Usando dicionário para simular switch-case
def opcao1():
    return "Você escolheu a opção 1."

def opcao2():
    return "Você escolheu a opção 2."

def opcao3():
    return "Você escolheu a opção 3."

# Mapeando opções para funções
switch = {
    1: opcao1,
    2: opcao2,
    3: opcao3
}

opcao = 2
resultado = switch.get(opcao, lambda: "Opção inválida.")()
print(resultado)

# 3. Usando lambda com dicionário
switch_lambda = {
    1: lambda: "Você escolheu a opção 1.",
    2: lambda: "Você escolheu a opção 2.",
    3: lambda: "Você escolheu a opção 3."
}

opcao = 3
resultado = switch_lambda.get(opcao, lambda: "Opção inválida.")()
print(resultado)

# 4. Usando classes para simular switch-case
class SwitchCase:
    def caso1(self):
        return "Você escolheu a opção 1."

    def caso2(self):
        return "Você escolheu a opção 2."

    def caso3(self):
        return "Você escolheu a opção 3."

    def default(self):
        return "Opção inválida."

switch_case = SwitchCase()
opcao = 1
metodo = getattr(switch_case, f'caso{opcao}', switch_case.default)
print(metodo())


"""
Resumo dos Exemplos:

    Estrutura if, elif e else: Verifica opções sequencialmente.
    Dicionário de funções: Mapeia opções para funções.
    Dicionário com lambdas: Usa expressões lambda para retornar resultados.
    Classes e getattr: Usa métodos de uma classe para simular opções.
"""