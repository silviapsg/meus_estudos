import os
import random
import string
from funcoes_padrao import continuar, terminar

# 1 - João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. 
# O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def calcular_gorjeta():
    os.system('cls')

    valor_conta = float(input('Digite o valor da conta: R$ '))
    porcentagem_gorjeta = float(input('Digite a porcentagem de gorjeta: '))
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    valor_total = valor_conta + valor_gorjeta

    print(f'Valor da gorjeta: R$ {valor_gorjeta:.2f}')
    print(f'Total a pagar: R$ {valor_total:.2f}')

    continuar()

# 2 - Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. 
# O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

def validar_cpf():
    os.system('cls')

    cpf = input('Digite seu CPF: ')

    if not cpf.isdigit():
        print('Erro: O CPF deve conter apenas número.')
    else: 
        if len(cpf) != 11:
            print('Erro: O CPF deve ter exatamente 11 dígitos.')
        else:
            print('CPF válido.')

    continuar()


# 3 - Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. 
# Isso ajudará a analisar a estrutura das palavras utilizadas.
# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

def contar_vogais():
    os.system('cls')

    texto = input('Digite um texto: ')
    cont = 0
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚâêôÂÊÔãõÃÕàÀ'

    for letra in texto:
        if letra in vogais:
            cont += 1
    print(f'O texto contém {cont} vogais.')

    continuar()

# 4 - Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
# Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.
# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

def identificar_palavras_longas():
    os.system('cls')

    texto = input('Digite um texto: ')
    palavras_longas = []

    for palavra in texto.split():
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    
    if palavras_longas:
        print(f'Palavras longas encontradas: {palavras_longas}')
    else:
        print(f'Nenhuma palavra longa foi encontradas no texto.')
    
    continuar()

# 5 - Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. 
# Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.
# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

def gerar_senha_aleatoria():
    caractere = string.ascii_letters + string.digits
    print('Senha gerada: ' + ''.join(random.choice(caractere) for _ in range(12)))

# 6 - Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. 
# Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.
# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. 
# O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:
# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

def criar_jogo():
    os.system('cls')

    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_usuario = input('Escolha: pedra, papel ou tesoura? ')
    escolha_computador = random.choice(opcoes)

    if escolha_usuario == 'pedra' and escolha_computador == 'tesoura':
        print(f'Computador escolheu: {escolha_computador}.')
        print('Você venceu!')
    elif escolha_usuario == 'tesoura' and escolha_computador == 'papel':
        print(f'Computador escolheu: {escolha_computador}.')
        print('Você venceu!')
    elif escolha_usuario == 'papel' and escolha_computador == 'pedra':
        print(f'Computador escolheu: {escolha_computador}.')
        print('Você venceu!')
    elif escolha_usuario == escolha_computador:
        print(f'Computador escolheu: {escolha_computador}')
        print('Empate!')
    else:
        print(f'Computador escolheu: {escolha_computador}')
        print('Você perdeu!')

    continuar()

# 7 - Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. 
# Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.
# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.
# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
# O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. 
# Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.

def adivinhar_numero():
    os.system('cls')

    numero = random.randint(1, 100)
    novo_palpite = 0

    while True: 
        try: 
            palpite = int(input('Tente adivinhar o número (1-100): '))

            if not 1 <= palpite <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            
            novo_palpite += 1

            if palpite > numero:
                print('Muito alto! Tente novamente.')
            elif palpite < numero:
                print('Muito baixo! Tente novamente.')
            else: 
                print(f'Parabéns! Você acertou o número {numero} em {novo_palpite} tentativas')
                break
        except ValueError as e:
            print(f'Entrada inválida: {e}')

    continuar()

# 8 - Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. 
# Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def criar_calculadora():
    os.system('cls')

    try:
        x = float(input('Digite o primeiro número: '))
        operacao = input('Escolha a operação (+, -, *, /): ')
        y = float(input('Digite o segundo número: '))
        
        if operacao == '+':
            resultado = x + y
        elif operacao == '-':
            resultado = x - y
        elif operacao == '*':
            resultado = x * y
        elif operacao == '/':
            resultado = x / y
        else:
            print('Operação inválida!')
        print(f'{x} {operacao} {y} = {resultado}')
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')

    continuar()

# 9 - Ana precisa de um programa simples para gerenciar suas tarefas diárias. 
# Ela quer poder adicionar, visualizar e remover tarefas de uma lista.
# Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. 
# Use uma lista para armazenar as tarefas.

def gerenciar_tarefas():  
    os.system('cls')
    tarefas = []

    while True:
        print('1. Adicionar tarefa')
        print('2. Visualizar tarefas')
        print('3. Remover tarefa')
        print('4. Sair\n')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            os.system('cls')
            tarefa = input('Digite a tarefa: ').strip()
            if tarefa:
                tarefas.append(tarefa)
                print('\nTarefa adicionada!\n')
            else: 
                print('\nErro: A tarefa não pode estar vazia.\n')
        elif opcao == 2:
            os.system('cls')
            if tarefas:
                print('Tarefas:')
                for i, tarefa in enumerate(tarefas, 1):
                    print(f'{i}. {tarefa}')
                print('\n')
            else:
                print("Nenhuma tarefa cadastrada.\n")
        elif opcao == 3:
            os.system('cls')
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.\n")
                continue
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Índice inválido! Digite um número válido.")
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")
        elif opcao == 4:
            os.system('cls')
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
    
    continuar()

# 10 - Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. 
# O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. 
# As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. 
# O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

def contar_cedulas():
    os.system('cls')
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input('Digite o valor do saque: R$ '))

        if valor <= 0:
            print('Erro: O valor deve ser positivo.')
        elif valor % 2 != 0:
            print('Erro: O valor deve ser múltiplo de 2.')
        else:
            print('Cédulas entregues: ')

            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f'{quantidade} cédulas de R$ {cedula}')
                    valor = valor % cedula
    except ValueError:
        print('Erro: Digite um valor numérico válido.')
    
    terminar()

def main():
    calcular_gorjeta()
    validar_cpf()
    contar_vogais()
    identificar_palavras_longas()
    gerar_senha_aleatoria()
    criar_jogo()
    adivinhar_numero()
    criar_calculadora()
    gerenciar_tarefas()
    contar_cedulas()

if __name__ == '__main__':
    main()