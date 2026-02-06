# Na Escola PythonVille, o professor quer registrar as notas dos alunos e depois consultar quem teve um bom desempenho.
# Além disso, a coordenação precisa manter um registro organizado com essas informações para uso futuro.
# O que você deve fazer:
# Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
# Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.

import csv, os
from funcoes_padrao import continuar, terminar

# Opção 1 - Lista de alunos já pronta (gravar e depois ler)

def listar_alunos():
    alunos = [['Ana', 85], ['Bruno', 60], ['Carlos', 72], ['Daniela', 90], ['Eduardo', 55]]

    with open('alunos.csv', 'w', newline='', encoding='UTF-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Nome', 'Nota'])
        escritor.writerows(alunos)

    print('Alunos com bom desempenho: ')
    with open('alunos.csv', 'r', encoding='UTF-8') as f:
        leitor = csv.reader(f)
        next(leitor)
        for nome, nota in leitor:
            if int(nota) >= 70:
                print(f'{nome} - {nota}')

    continuar()

# Opção 2 - Usuário digita nome e data

def digitar_alunos():
    os.system('cls')
    alunos = []
    quantidade = int(input('Quantos alunos deseja cadastrar? '))

    for i in range (quantidade):
        nome = input('Digite o nome do aluno: ')
        nota = int(input('Digite a nota: '))
        alunos.append([nome,nota])

    with open('alunos2.csv','w', newline='', encoding='UTF-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Nome','Nota'])
        escritor.writerows(alunos)

    print('Alunos com bom desempenho: ')
    with open('alunos2.csv', 'r', encoding='UTF-8') as f:
        leitor = csv.reader(f)
        next(leitor)
        for nome, nota in leitor:
            if int(nota) >= 70:
                print(f'{nome} - {nota}')

    terminar()

def main():
    listar_alunos()
    digitar_alunos()

if __name__ == '__main__':
    main()

