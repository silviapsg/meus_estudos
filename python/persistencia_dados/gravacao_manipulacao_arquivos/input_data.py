nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

with open('input_data.txt', 'a', encoding='UTF-8') as f:
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')