import re

# STRINGS
# Aspas simples ou duplas podem ser usadas, conforme a preferência ou contexto.
mensagem = 'Olá, mundo!'
print(mensagem)
mensagem = "Python é incrível"
print(mensagem)

# Aspas triplas permitem criar strings de múltiplas linhas com quebras de linha.
texto = """Essa é uma string 
que pode ter múltiplas 
linhas."""
print(texto)

# As f-strings permitem a formatação de strings de forma simples e legível, incorporando expressões e variáveis diretamente no texto.
estudante = "Pedro"
nota = 10
mensagem = f"{estudante} tirou a nota {nota}!"
print(mensagem)

# A indexação permite acessar caracteres individuais de um string através de seu índice, começando de 0 para o primeiro caractere.
# Para acessar caracteres a partir do final, usa-se índice negativos, onde -1 é o último caractere.
texto = "Python"
print(texto[5])
print(texto[-1])

# O slicing permite extrair uma parte da string.
# A sintaxe é string[início:fim:passo]
texto = "Python"
print(texto[1:4])   # Extrai os caracteres da posição 1 até a posição 3 (não incluindo o índice 4), resultando em 'yth'.
print(texto[:3])    # Extrai os primeiros 3 caracteres, resultando em 'Pyt'.
print(texto[::2])   # Extrai os caracteres de forma alternada, pegando um a cada dois, resultando em 'Pto'

# O operador in verifica se uma substring está presente em uma string.
# Ele retorna True se a substring estiver presente na string e False caso contrário.
texto = "Python"
print("Py" in texto)
print("Java" in texto)

# O método startswith() verifica se a string começa com uma substring específica.
# Ele retorna True se a string iniciar com a substring especificada e False caso contrário.
texto = "Python"
print(texto.startswith("Py"))
print(texto.startswith("py"))

# O método endswith() verifica se a string termina com uma substring específica.
# Ele retorna True se a string finalizar com a substring especificada e False caso contrário.
texto = "Python"
print(texto.endswith("on"))
print(texto.endswith("ton"))

# EXPRESSÕES REGULARES (REGEX)
texto = "Entre em contato pelo email support@example.com"
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
resultado = re.search(padrao_email, texto)
if resultado:
    print("Email encontrado: ", resultado.group())
else: 
    print("Nenhum email encontrado.")
