'''
Esturura do CONJUNTO:

conjunto = {x, y, z}
conjunto_misto = {1, 'texto', 3.14, True}
# Conjuntos são coleções não ordenadas, não indexadas e não permitem elementos duplicados

Estrutura do DICIONÁRIO:

dicionario = {'chave1': valor1, 'chave2': valor2}
dicionario_misto = {
    'nome': 'Maria',
    'idade': 30,
    'altura': 1.65,
    'ativo': True,
    'hobbies': ['leitura', 'treino']
}
# Dicionários armazenam dados em pares chave-valor, onde as chaves são únicas e imutáveis.
'''

import os
from funcoes_padrao import continuar, terminar

# 1 - Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições, pois algumas pessoas foram convidadas mais de uma vez por engano. 
# Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
# Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

def organizar_lista_convidados():
    convidados = set()

    while True:
        convidado = input('Digite o nome do convidado ou "sair" para encerrar: ')
        
        if convidado.lower() =='sair':
            break

        convidados.add(convidado)

    print(f'Convidados confirmados: {', '.join(convidados)}')

    continuar()

# 2 - Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. 
# Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

def descobrir_palavras_comuns():
    os.system('cls')
    texto1 = set(input('Texto 1: ').lower().split())
    texto2 = set(input('Texto 2: ').lower().split())
    comuns = texto1.intersection(texto2)
    print(f'Palavras em comum: {comuns}')
    continuar()

# 3 - Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
# Elas querem um programa que mostre:
#   Quais itens apareceram nas duas listas
#   Quais foram exclusivos de Laura
#   Quais foram exclusivos da Ana
# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

def comparar_listas_compra():
    os.system('cls')
    laura = set(input('Lista de Laura: ').split(', '))
    ana = set(input('Lista de Ana: ').split(', '))
    comuns = laura.intersection(ana)
    exclusivos_laura = laura.difference(ana)
    exclusivos_ana = ana.difference(laura)
    print(f'Itens em ambas as listas: {', '.join(comuns)}')
    print(f'Itens exclusivos de Laura: {', '.join(exclusivos_laura)}')
    print(f'Itens exclusivos de Ana: {', '.join(exclusivos_ana)}')
    continuar()

# 4 - Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. 
# Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.
def verificar_permissoes():
    os.system('cls')
    permissoes_principais = set(input('Permissões principais: ').strip().lower().split(', '))
    permissoes_solicitadas = set(input('Permissões solicitadas: ').strip().lower().split(', '))
    eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

    if eh_subconjunto:
        print('As permissões solicitadas fazem parte das permissões principais.')
    else:
        print('As permissões solicitadas não fazem parte das permissões principais.')

    continuar()

# 5 - Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
# Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. 
# Sua tarefa é criar um programa que realize essa operação.

def comparar_conjunto_numeros():
    os.system('cls')
    equipe_a = {'planejar reunião', 'revisar documento', 'testar sistema'} 
    equipe_b = {'testar sistema', 'implementar funcionalidade', 'corrigir bug'} 
    tarefas_combinadas = equipe_a.union(equipe_b)
    print(f'Tarefas: {tarefas_combinadas}')
    tarefa_remover = input('Tarefa a ser removida: ').lower()

    if tarefa_remover in tarefas_combinadas:
        tarefas_combinadas.remove(tarefa_remover)
    print(f'Tarefas finais: {tarefas_combinadas}')

    continuar()

# 6 - Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. 
# Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. 
# O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

def cadastrar_produtos():
    os.system('cls')
    produtos = {}

    for i in range(3):
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade: '))
        produtos[nome] = quantidade
    print(f'Dicionário de produtos: {produtos}')

    continuar()

# 7 - Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. 
# Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

def atualizar_informacoes_estoque():
    os.system('cls')
    estoque = { 
        "Caderno universitário": 50, 
        "Caneta azul": 120, 
        "Borracha branca": 30 
    } 
    print(f'Estoque: ')
    produto = input('Digite o nome do produto a ser atualizado: ')

    if produto in estoque:
        nova_quantidade = int(input('Digite a nova quantidade: '))
        estoque[produto] = nova_quantidade
        print('Quantidade atualizada com sucesso!')
        print(estoque)
    else:
        print('Produto não encontrado no estoque.')
    
    continuar()

# 8 - Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. 
# Agora, ele precisa de um programa que apresente três informações:
#   Os nomes de todos os participantes.
#   As idades de todos os participantes.
#   Uma relação completa com o nome e a idade de cada um.
# Sua tarefa é criar esse programa com base nas informações fornecidas.

def analisar_participantes_maratona():
    os.system('cls')
    participantes = { 
        "Mariana": 25, 
        "Carlos": 32, 
        "Beatriz": 28, 
        "Rafael": 35 
    } 

    print(f'Nome dos participantes: {', '.join(participantes.keys())}')
    print(f'Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}') 
    print('Participantes e suas idades:') 

    for nome, idade in participantes.items(): 
        print(f'- {nome}: {idade} anos') 

    continuar()

# 9 - Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. 
# O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
# O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

def gerenciar_inscricoes_workshop():
    os.system('cls')
    participantes = { 
        'Workshop 1': {'Alice', 'Bruno', 'Carla', 'Diego'}, 
        'Workshop 2': {'Fernanda', 'Gustavo', 'Helena'} 
    } 
    nome_remover = input('Digite o nome do participante a ser removido: ')

    for workshop, nomes in participantes.items():
        nomes.discard(nome_remover)
    print('Lista atualizada de participantes: ')

    for workshop, nomes in participantes.items():
        print(f'{workshop}: {nomes}')

    continuar()

# 10 - Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. 
# Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. 
# Sua tarefa é criar um programa que exiba o total de vendas por categoria.

def analisar_vendas_categoria():
    os.system('cls')
    
    vendas = {
        'Eletrônicos': [ 
            {'produto': 'Smartphone', 'quantidade': 5, 'valor_unitario': 2000}, 
            {'produto': 'Tablet', 'quantidade': 3, 'valor_unitario': 1500} 
        ], 
        'Eletrodomésticos': [ 
            {'produto': 'Geladeira', 'quantidade': 2, 'valor_unitario': 3000}, 
            {'produto': 'Micro-ondas', 'quantidade': 4, 'valor_unitario': 800} 
        ], 
        'Livros': [ 
            {'produto': 'Livro A', 'quantidade': 10, 'valor_unitario': 50}, 
            {'produto': 'Livro B', 'quantidade': 5, 'valor_unitario': 100} 
        ] 
    } 
    print('Total de vendas por categoria:')

    for categoria, itens in vendas.items():
        total = 0
        for item in itens:
            total += item['quantidade'] * item['valor_unitario']
        print(f'- {categoria}: R$ {total:.2f}')
    
    terminar()

def main():
    organizar_lista_convidados()
    descobrir_palavras_comuns()
    comparar_listas_compra()
    verificar_permissoes()
    comparar_conjunto_numeros()
    cadastrar_produtos()
    atualizar_informacoes_estoque()
    analisar_participantes_maratona()
    gerenciar_inscricoes_workshop()
    analisar_vendas_categoria()

if __name__ == '__main__':
    main()