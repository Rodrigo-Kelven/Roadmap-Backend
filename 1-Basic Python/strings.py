# Criando uma string de exemplo
texto = "Python é uma linguagem de programação."

# 1. upper()
print(texto.upper())  # Converte a string para maiúsculas

# 2. lower()
print(texto.lower())  # Converte a string para minúsculas

# 3. title()
print(texto.title())  # Converte a primeira letra de cada palavra para maiúscula

# 4. strip()
print(texto.strip())  # Remove espaços em branco no início e no final da string

# 5. split()
palavras = texto.split()  # Divide a string em uma lista de palavras
print(palavras)

# 6. join()
nova_string = " ".join(palavras)  # Junta uma lista de palavras em uma única string
print(nova_string)

# 7. replace()
nova_frase = texto.replace("Python", "Java")  # Substitui uma substring por outra
print(nova_frase)

# 8. find()
indice = texto.find("linguagem")  # Retorna o índice da primeira ocorrência da substring
print(indice)

# 9. count()
contagem = texto.count("a")  # Conta quantas vezes uma substring aparece na string
print(contagem)

# 10. startswith()
print(texto.startswith("Python"))  # Verifica se a string começa com a substring

# 11. endswith()
print(texto.endswith("."))  # Verifica se a string termina com a substring

# 12. isdigit()
numero = "12345"
print(numero.isdigit())  # Verifica se todos os caracteres são dígitos

# 13. isalpha()
letras = "Python"
print(letras.isalpha())  # Verifica se todos os caracteres são letras

# 14. isalnum()
alfa_num = "Python3"
print(alfa_num.isalnum())  # Verifica se todos os caracteres são letras ou dígitos

# 15. format()
nome = "Mundo"
mensagem = "Olá, {}!".format(nome)  # Formata a string com substituição
print(mensagem)

# 16. f-strings (Python 3.6+)
mensagem_f = f"Olá, {nome}!"  # Formatação com f-strings
print(mensagem_f)

# 17. capitalize()
print(texto.capitalize())  # Converte a primeira letra da string para maiúscula

# 18. swapcase()
print(texto.swapcase())  # Troca maiúsculas por minúsculas e vice-versa

# 19. zfill()
numero_completo = "42".zfill(5)  # Preenche a string com zeros à esquerda
print(numero_completo)

# 20. title()
print(texto.title())  # Converte a primeira letra de cada palavra para maiúscula


