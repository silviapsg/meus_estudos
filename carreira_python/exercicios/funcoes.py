'''
Estrutura da função:

def nome_da_funcao(parametro):
    Bloco de código
    return parametro

nome_da_funcao(parametro)
'''

import datetime
import os
from funcoes_padrao import continuar, terminar

# 1 - Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
# Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade():
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    
    print(f'A idade é {idade} anos.')

    continuar()

# 2- Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def calcular_caracteres():
    os.system('cls')

    palavra = input('Digite uma palavra: ')
    quantidade_caracteres = len(palavra)

    print(f'Essa palavra tem {quantidade_caracteres} caracteres.')

    continuar()

# 3 - Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
# Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
# O sistema deverá ter a seguinte regra:
# Se for antes das 12h, exibir "Bom dia";
# Entre 12h e 18h, exibir "Boa tarde";
# Após 18h, exibir "Boa noite".

def exibir_saudacao():
    os.system('cls')

    hora_atual = datetime.datetime.now().hour

    if hora_atual < 12:
        print('Bom dia!')
    elif 12 <= hora_atual < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')

    continuar()

# 4 - Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. 
# No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

def converter_telefones():
    os.system('cls')

    telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
    lista_convertida = []

    for telefone in telefones:
        telefone_convertido = int(telefone)
        lista_convertida.append(telefone_convertido)
        
    return lista_convertida

def verificar_tipos(lista):
    for numero in lista:
        print(numero, type(numero))
    
    continuar()

# 5 - Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
# As vendas são informadas em uma única linha separadas por espaços.
# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

def calcular_vendas():
    os.system('cls')

    linha = input('Digite os valores das vendas: ')
    vendas_separadas = linha.split()
    vendas = [float(v) for v in vendas_separadas]
    total = sum(vendas)

    print(f'Valores separados: {vendas}')
    print(f'O total de vendas foi: {total}')  

    continuar()

# 6 - Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

def gerar_relatorios():
    os.system('cls')

    numeros = input('Digite os números separados por espaço: ').split()
    pares = filter(lambda x: int(x) %2 == 0, numeros)

    print('Números pares:', ' '.join(pares))

    continuar()

# 7 - Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. 
# Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
# Crie um programa que junte as listas e exiba o resultado no formato produto: preço

def exibir_listas():
    os.system('cls')

    produtos = input('Digite os produtos separados por vírgula: ').split(',')
    print(produtos)
    precos = input('Digite os preços separados por vírgula: ').split(',')
    print(precos)

    for produto, preco in zip(produtos, precos):
        print(f'{produto.strip()}: {preco.strip()}')

    continuar()

# 8 - Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

def criar_calculadora():
    os.system('cls')

    somar = lambda x, y: x + y
    subtrair = lambda x, y: x - y
    multiplicar = lambda x, y: x * y
    dividir = lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero'

    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo números: '))
    operacao = input('Escolha a operação (| + | - | * | / |): ')

    if operacao == '+':
        print(f'O resultado é: {somar(x,y)}')
    elif operacao == '-':
        print(f'O resultado é: {(subtrair(x,y))}')
    elif operacao == '*':
        print(f'O resultado é: {(multiplicar(x,y))}')
    elif operacao == '/':
        print(f'O resultado é: {(dividir(x,y))}')
    else:
        print('Operação inválida!')
    
    continuar()

# 9 - Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

def aplicar_desconto():
    os.system('cls')

    porcentagem = float(input('Digite a porcentagem de desconto: '))
    valor = float(input('Digite o valor da compra: R$ '))
    valor_final = valor - (valor * (porcentagem / 100))

    print(f'Preço final com desconto: R$ {valor_final}')

    continuar()

# 10 - Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. 
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
# Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def calcular_numeros():
    os.system('cls')

    numero = int(input('Digite um número: '))
    soma = 0

    for i in range(1, numero + 1):
        soma += i
        print(f'i = {i}, soma = {soma}')

    print(f'A soma de 1 a {i} é: {soma}')
        
    terminar()

def main():
    calcular_idade()
    calcular_caracteres()
    exibir_saudacao()
    telefones_convertidos = converter_telefones()
    verificar_tipos(telefones_convertidos)
    calcular_vendas()
    gerar_relatorios()
    exibir_listas()
    criar_calculadora()
    aplicar_desconto()
    calcular_numeros()

if __name__ == '__main__':
    main()