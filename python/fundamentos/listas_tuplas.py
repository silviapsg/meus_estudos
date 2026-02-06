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

# 3 - Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação.
# À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
# Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

def registrar_voluntarios():
    os.system('cls')

    voluntarios = []

    while True:
        voluntario = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
        if voluntario.lower() == 'sair':
            break
        else: 
            voluntarios.append(voluntario)

    print(f'\nVoluntários registrados: {voluntarios}')

    continuar()

# 4 - Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

def unir_relatorios():
    os.system('cls')

    estoque1 = ('Arroz', 'Feijão', 'Macarrão')
    estoque2 = ('Óleo', 'Sal', 'Açúcar')
    print(f'Estoque de produtos 1: {estoque1}')
    print(f'Estoque de produtos 2: {estoque2}')

    estoque_unificado = estoque1 + estoque2
    print(f'Estoque combinado: {estoque_unificado}')

    continuar()

# 5 - Camila adora receber amigos para jantares temáticos. 
# Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
# Camila quer adicionar novos nomes e organizá-los em posições específicas.
# Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

def reorganizar_lista():
    os.system('cls')

    convidados = ['Ana', 'Pedro', 'Carlos']
    print(f'Lista atual de convidados: {convidados}')

    novo_convidado = input('Digite o nome do novo convidado: ')
    posicao = int(input('Digite a posição na qual deseja inserir o condidado: '))
    convidados.insert(posicao - 1, novo_convidado)
    print(f'Lista atualizada de convidados: {convidados}')

    continuar()

# 6 - A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante. 
# Os eventos foram registrados na ordem inversa à que deveriam acontecer. 
# Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.
# Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.
# eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

def ordenar_eventos():
    os.system('cls')

    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    print(f'Ordem original: {eventos_registrados}')
    eventos_registrados.reverse()
    print(f'Ordem corrigida: {eventos_registrados}')

    continuar()


# 7 - O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
# Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

def corrigir_nome():
    os. system('cls')

    atletas = ['Ana', 'Carlos', 'Pedro']
    print(f'Lista original: {atletas}')

    nome_incorreto = input('Digite o nome incorreto: ')
    if nome_incorreto in atletas:
        nome_correto = input('Digite o nome correto: ')
        posicao = atletas.index(nome_incorreto)
        atletas.remove(nome_incorreto)
        atletas.insert(posicao, nome_correto)
        print(f'O nome {nome_incorreto} foi substituído por {nome_correto}')
        print(f'Lista atualizada: {atletas}')
    else:
        print('Nome não encontrado.')

    continuar() 

# 8 - Paulo está criando uma lista de pedidos para a lanchonete.
# Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.
# Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.

def remover_item():
    os.system('cls')

    pedidos = input('Pedidos feitos (separados por vírgula): ').split(', ')
    pedidos.pop()
    print(f'Pedidos finais: {pedidos}')

    continuar()

# 9 - A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. 
# Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.
# Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

def calcular_media():
    os.system('cls')

    notas = input('Digite as notas dos alunos separadas por vírgulas: ').split(', ')
    notas = [float(nota) for nota in notas]
    media = sum(notas) / len(notas)
    print(f'Média final da turma: {media:.2f}')

    continuar()

# 10 - Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
# Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. 
# Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:
# Aluno: Nome
# Idade: Idade
# Nota: Nota
# Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

def registrar_alunos():
    dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separadas por vírgulas: ').split(', ')

    for i in range(0, len(dados), 3):
        nome, idade, nota = dados[i], int(dados[i+1]), float(dados[i+2])
        print(f'Aluno: {nome}')
        print(f'Idade: {idade}')
        print(f'Nota: {nota}\n')
    
    terminar()

def main():
    verificar_itens()
    organizar_notas()
    registrar_voluntarios()
    unir_relatorios()
    reorganizar_lista()
    ordenar_eventos()
    corrigir_nome()
    remover_item()
    calcular_media()
    registrar_alunos()

if __name__ == '__main__':
    main()