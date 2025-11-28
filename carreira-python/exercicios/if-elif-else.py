'''
Estrutura IF/ELIF/ELSE:

IF (condição):
    # Executa este bloco se a condição for verdadeira.
ELIF (outra condição):
    # Executa este bloco se a condição anterior for falsa e esta nova condição for verdadeira.
ELSE:
    # Executa este bloco se nenhuma das condições anteriores for verdadeira.

Observações:
- Pode haver vários ELIFs;
- O ELSE é opcional, mas só pode existir um;
- A ordem das condições importa.
'''

import os
import sys

# 1 - Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
# Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
# Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
# Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

def monitorar_venda():
    macas = int(input('Digite a quantidade de maçãs vendidas: '))
    bananas = int(input('Digite a quantidade de bananas vendidas: '))

    if macas > bananas:
        print('As maçãs tiveram mais vendas.')
    elif bananas > macas:
        print('As bananas tiveram mais vendas.')
    else:
        print('Bananas e maçãs tiveram a mesma quantidade de vendas.')

    continuar()

# 2 - Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
# No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
# Se algum valor for negativo, mostre uma mensagem informando o erro.

def calcular_tempo_de_projeto():
    os.system('cls')

    a = int(input('Informe os dias para a atividade A: '))
    b = int(input('Informe os dias para a atividade B: '))
    c = int(input('Informe os dias para a atividade C: '))

    if (a >= 0 and b >= 0 and c >= 0):
        total = a + b + c
        print(f'O tempo total do projeto é de {total} dias.')
    else:
        print('Erro: Os dias não podem ser negativos.')

    continuar()

# 3 - Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
# Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

def verificar_temperatura():
    os.system('cls')

    temperatura = int(input('Digite a temperatura atual: '))

    if temperatura > 25:
        print('Alerta! Temperatura acima do limite permitido.')
    else: 
        print('Temperatura dentro do limite seguro.')

    continuar()

# 4 - Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. 
# O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
# Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2)
# Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

def calcular_imc():
    os.system('cls')
    
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura**2)
    print(f'Seu IMC é: {imc:.2f}')

    if imc > 25:
        print('Você está acima do peso.')
    elif 18.5 <= imc < 25:
        print('Vocês está no peso normal.')
    else:
        print('Você está abaixo do peso')
    
    continuar()

# 5 - Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
# Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
# O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

def controlar_orcamento():
    os.system('cls')

    limite = 3000
    despesas = float(input('Digite o valor total de despesas do mês (R$): '))

    if despesas <= limite:
        print('Vocês está dentro do orçamento.')
    else:
        print('Atenção! Você ultrapassou o limite do orçamento.')

    continuar()

# 6 - Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. 
# Para isso, ela usará o horário atual. 
# O escritório só permite acesso entre 8h e 18h. 
# Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

def controlar_acesso():
    os.system('cls')

    hora_atual = int(input('Digite a hora atual (formato 24 horas): '))

    if (8<= hora_atual < 18):
        print('Acesso permitido.')
    else:
        print('Acesso negado.')

    continuar()

# 7 - Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. 
# As regras são:
# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. 
# Com base na média, exiba a situação do aluno.

def calcular_media():
    os.system('cls')

    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    media = (n1 + n2 + n3) / 3

    if media >= 7:
        print('Aprovado!')
    elif (5 <= media < 7):
        print('Recuperação!')
    else: 
        print('Reprovado!')

    continuar()

# 8 - Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
# O valor do pedágio depende da distância percorrida:
# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

def calcular_pedagio():
    os.system('cls')

    distancia = int(input('Digite a distância percorrida (em km): '))

    if distancia < 100:
        print('Valor do pedágio: R$ 10,00')
    elif (100 <= distancia <= 200):
        print('Valor do pedágio: R$ 20,00')
    else: 
        print('Valor do pedágio: R$ 30,00')

    continuar()

# 9 - Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
# Essa verificação será usada para definir ações diferentes dentro do jogo. 
# Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

def verificar_numero():
    os.system('cls')

    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        print('É par!')
    else:
        print('É ímpar!')

    continuar()

# 10 - Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
# O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

def aprovar_emprestimo():
    os.system('cls')

    renda = float(input('Digite o valor da sua renda mensal: R$ '))
    parcela = float(input('Digite o valor da parcela desejada: R$ '))

    if (renda > 2000) and (parcela <= (renda * 0.30)):
        print(f'Empréstimo aprovado!')
    elif renda <= 200:
        print('Empréstimo negado: renda insuficiente!')
    else: 
        print('Empréstimo negado: parcela acima de 30% da renda!\n')

    terminar()

def continuar():
    input('\nDigite uma tecla para avançar para a próxima atividade ')

def terminar ():
    print('Finalizando as atividades... Até mais!')
    sys.exit()

def main():
    monitorar_venda()
    calcular_tempo_de_projeto()
    verificar_temperatura()
    calcular_imc()
    controlar_orcamento()
    controlar_acesso()
    calcular_media()
    calcular_pedagio()
    verificar_numero()
    aprovar_emprestimo()

if __name__ == '__main__':
    main()