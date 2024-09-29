# 1. Estrutura básica if
numero = 10
if numero > 5:
    print("O número é maior que 5.")

# 2. Usando else
numero = 3
if numero > 5:
    print("O número é maior que 5.")
else:
    print("O número não é maior que 5.")

# 3. Usando elif
numero = 5
if numero > 5:
    print("O número é maior que 5.")
elif numero == 5:
    print("O número é igual a 5.")
else:
    print("O número é menor que 5.")

# 4. Verificando múltiplas condições
nota = 85
if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
else:
    print("Nota: D ou F")

# 5. Condições compostas
idade = 18
possui_habilitacao = True
if idade >= 18 and possui_habilitacao:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# 6. Usando or para condições
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("É fim de semana!")

# 7. Verificando presença em uma lista
fruta = "maçã"
if fruta in ["maçã", "banana", "laranja"]:
    print("Fruta disponível.")

# 8. Verificando se um número é par ou ímpar
numero = 7
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 9. Usando operadores de comparação
a = 10
b = 20
if a < b:
    print("a é menor que b.")
elif a > b:
    print("a é maior que b.")
else:
    print("a é igual a b.")

# 10. Usando condicional ternária
resultado = "Aprovado" if nota >= 60 else "Reprovado"
print("Resultado:", resultado)


"""
Resumo dos Exemplos:

    Estrutura básica if: Verifica uma condição simples.
    else: Ação alternativa quando a condição do if é falsa.
    elif: Verifica múltiplas condições.
    Múltiplas condições: Avalia a nota em categorias.
    Condições compostas: Usa and para combinar condições.
    Usando or: Verifica se um dia é fim de semana.
    Verificação em lista: Verifica se uma fruta está disponível.
    Par ou ímpar: Usa o operador módulo para verificação.
    Operadores de comparação: Compara dois valores.
    Condicional ternária: Sintaxe concisa para atribuição baseada em condição.
"""