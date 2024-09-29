# 1. Contador simples
contador = 0
print("Contador de 0 a 4:")
while contador < 5:
    print(contador)
    contador += 1

# 2. Loop com condição
numero = 0
print("\nSoma de números até 10:")
while numero < 10:
    numero += 1
print("Número final:", numero)

# 3. Loop infinito (com break)
print("\nLoop infinito (controlado por break):")
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta.lower() == 'sair':
        break

# 4. Usando continue para pular iterações
print("\nUsando continue para pular números ímpares:")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 != 0:
        continue
    print(numero)

# 5. Validação de entrada do usuário
print("\nValidação de entrada do usuário:")
senha_correta = "1234"
senha = ""
while senha != senha_correta:
    senha = input("Digite a senha: ")
print("Senha correta!")

# 6. Contagem regressiva
import time

print("\nContagem regressiva:")
contagem = 5
while contagem > 0:
    print(contagem)
    time.sleep(1)  # Pausa de 1 segundo
    contagem -= 1
print("Fim!")

# 7. Soma de números até que o usuário digite zero
soma = 0
print("\nSoma de números (digite 0 para encerrar):")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma += numero
print("Soma total:", soma)

# 8. Uso de flags
print("\nUso de flag para controle de loop:")
flag = True
while flag:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() == 'n':
        flag = False
print("Loop encerrado.")

# 9. Contagem com controle de entrada do usuário
contagem = 0
print("Contagem até 5 (digite 'sair' para parar):")
while contagem < 5:
    entrada = input(f"Contagem atual: {contagem}. Digite 'sair' para parar ou pressione Enter para continuar: ")
    if entrada.lower() == 'sair':
        break
    contagem += 1
print("Contagem final:", contagem)

# 10. Validação de entrada numérica
while True:
    entrada = input("Digite um número positivo (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        if numero < 0:
            print("Por favor, digite um número positivo.")
        else:
            print(f"Número digitado: {numero}")
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# 11. Contagem regressiva com sleep
import time
contagem_regressiva = 5
print("Contagem regressiva:")
while contagem_regressiva > 0:
    print(contagem_regressiva)
    time.sleep(1)
    contagem_regressiva -= 1
print("Fim!")

# 12. Loop infinito controlado por flag
running = True
while running:
    comando = input("Digite 'parar' para encerrar: ")
    if comando.lower() == 'parar':
        running = False
print("Loop encerrado.")

# 13. Utilizando um iterador com `next()`
numeros = [1, 2, 3, 4, 5]
iterador = iter(numeros)
while True:
    try:
        numero = next(iterador)
        print(numero)
    except StopIteration:
        break

# 14. FizzBuzz com while
numero = 1
print("FizzBuzz até 20:")
while numero <= 20:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero += 1

# 15. Usando `continue` para pular condições
numero = 0
print("Números pares de 0 a 10:")
while numero <= 10:
    numero += 1
    if numero % 2 != 0:
        continue
    print(numero)

# 16. Usando um dicionário para um menu interativo
menu = {
    "1": "Opção 1: Fazer algo.",
    "2": "Opção 2: Fazer outra coisa.",
    "3": "Sair."
}

while True:
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}: {value}")
    escolha = input("Escolha uma opção: ")
    if escolha == "3":
        print("Saindo...")
        break
    elif escolha in menu:
        print(f"You selected: {menu[escolha]}")
    else:
        print("Opção inválida, tente novamente.")

# 17. Jogo de adivinhação
import random

numero_secreto = random.randint(1, 10)
tentativas = 0
print("\nAdivinhe o número entre 1 e 10:")
while True:
    palpite = int(input("Digite seu palpite (ou 0 para sair): "))
    if palpite == 0:
        print("Saindo do jogo.")
        break
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Você adivinhou em {tentativas} tentativas!")
        break



"""
Resumo dos Exemplos:

    Contador simples: Loop que conta até 4.
    Loop com condição: Incrementa um número até atingir um limite.
    Loop infinito: Exemplo controlado com break.
    continue: Pula iterações específicas.
    Validação de entrada: Loop até que a senha correta seja digitada.
    Contagem regressiva: Exibe contagem regressiva com pausa.
    Soma de números: Soma números até que o usuário digite zero.
    Uso de flags: Controla a continuidade do loop.
"""