'''
Estrutura FOR:

FOR (variável) IN (sequência):
    # Executa este bloco para cada item da sequência (lista, tupla, string, range, etc).
    # A variável assume o valor de cada elemento a cada iteração.

Observações FOR:
- O número de iterações é determinado pelo tamanho da sequência.
- Pode ser usado com break (interrompe o loop) e continue (pula para a próxima iteração).
    
Estrutura WHILE:

WHILE (condição):
    # Executa este bloco equando a condição for verdadeira.
    # O loop termina quando a condição se torna falsa.

Observações WHILE:
- O loop pode ser infinito se a condição nunca se tornar falsa.
- Também pode usar break e continue para controlar o fluxo.
- Útil quando não sabemos previamente quantas vezes precisamos iterar.
'''

import os

# 1 - Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
# Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.
# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
# Ajude Ana a decidir entre usar um laço for ou while. 
# Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.

def processar_nomes():
    '''
        Nesse caso, o laço FOR é o mais adequado, pois o número exato de elementos na lista já é conhecido. 
        Logo, todos os itens serão percorridos de maneira clara e direta, sem precisar gerenciar manualmente um contador ou condição de parada.
    '''

    clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

    for cliente in clientes:
        print(cliente)

    continuar()

# 2 - André está testando um novo recurso no backend do Buscante que processa dados em um loop. 
# Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
# contador = 0
# while contador < 10:
#     print("Processando dados...")
# Qual é o problema do código de André e como resolver? 

def testar_recurso():
    '''
        Nesse caso, o recurso está em loop porque a condição de parada nunca será alcançada (contador sempre será 0). 
        Para evitar isso, é necessário garantir que o valor do contador seja atualizado dentro do loop, permitindo que a condição seja eventualmente falsa.
    '''
    os.system('cls')
    contador = 0

    while contador < 10:
        print('Processando dados...')
        contador += 1

    continuar()

def continuar ():
    input('\nDigite uma tecla para avançar para a próxima atividade ')

def main():
    processar_nomes()
    testar_recurso()

if __name__ == '__main__':
    main()