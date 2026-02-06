import os

restaurantes = [{'nome':'BK', 'categoria':'Fast Food', 'ativo':False},
                {'nome':'Bobs', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'Spoleto', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_programa():
    '''Essa função é responsável por exibir o nome do programa na tela.'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções disponíveis no menu principal.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo estilizado na tela.
    
    Inputs:
    - Texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal():
    '''Essa função é responsável por solicitar que o usuário digite uma tecla para voltar ao menu principal.'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante.
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novo restaurante')

    restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome categoria do restaurante {restaurante}: ')
    dados_restaurante = {'nome':restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {restaurante} foi cadastrado com sucesso')

    voltar_menu_principal()

def listar_restaurante():
    '''Essa função é responsável por listar os restaurantes cadastrados.
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes cadastrados')
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_menu_principal()
    
def ativar_restaurante():
    '''Essa função é responsável por alterar o estado de um restaurante cadastrado.
    
    Inputs:
    - Nome do restaurante

    Outputs:
    - Exibe uma mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando o estado dos restaurantes cadastrados')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_menu_principal()

def finalizar_app():
    '''Essa função é responsável por exibir uma mensagem de finalização do app.
    
    Outputs:
    - Retorna ao menu principal
    '''
    exibir_subtitulo('Finalizando o app...')

def opcao_invalida():
    '''Essa função é responsável por exibir uma mensagem de opção inválida e retornar ao menu principal.
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!')
    voltar_menu_principal()

def escolher_opcoes():
    '''Essa função é responsável por solicitar e executar a opção escolhida pelo usuário.
    
    Inputs:
    - Opção escolhida

    Outputs:
    - Executa a opção escolhida pelo usuário.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if (opcao_escolhida == 1):
            cadastrar_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurante()
        elif (opcao_escolhida == 3):
            ativar_restaurante()
        elif (opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a função principal que é responsável por iniciar o programa.'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()