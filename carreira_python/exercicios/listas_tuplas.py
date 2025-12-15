'''
Esturura da LISTA:

lista = [ x, y, z]
lista_mista = [1, 'texto', 3.14, True, [1, 2, 3]]
# Lista são flexíveis e podem conter qualquer tipo de dado, misturando-os conforme necessário.

Estrutura da TUPLA:

tupla = (x, y, z)
tupla_mista = (1, 'texto', 3.14, False, [1, 2, 3])
# Embora tuplas sejam imutáveis, elas podem conter qualquer tipo de dado, incluindo listas ou outras tuplas.
'''

# 1 - Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. 
# Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

import os
from funcoes_padrao import continuar, terminar

def verificar_itens():
    itens = ['arroz', 'feijão', 'óleo']
    item = input('Digite o item que você quer verificar: ')
    if item in itens: 
        print(f'O item {item} já está disponível na despensa.')
    else:
        print(f'O item {item} precisa ser comprado.')

    continuar()

# 2 - Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. 
# Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.
# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

def organizar_notas():
    os.system('cls')

    notas = [85, 70, 90, 60, 75]
    print(f'Notas: {notas}')
    
    notas.sort()
    print(f'Notas ordenadas: {notas}')

    continuar()
   
def main():
    verificar_itens()
    organizar_notas()

if __name__ == '__main__':
    main()