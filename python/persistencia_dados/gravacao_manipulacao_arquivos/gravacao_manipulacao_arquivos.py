'''
Por que usar arquivos?
- Armazenar
- Compartilhar
- Persistir

Função open():
- Escreve arquivos
- Lê arquivos
'''

import csv, json

# Arquivo .txt com a função open()
with open('dados.txt', 'w', encoding='UTF-8') as f:
    f.write('Olá, mundo!')

with open('dados.txt', 'r', encoding='UTF-8') as f:
    conteudo = f.read()
    print(conteudo)

with open('dados.txt', 'a', encoding='UTF-8') as f:
    f.write('\nÚltima linha')

with open('dados.txt', 'r', encoding='UTF-8') as f:
    conteudo = f.read()
    print(conteudo)

# Arquivo .csv com a função open()
with open('dados.csv', 'w', encoding='UTF-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nome','idade'])
    escritor.writerow(['Ana', 32])

with open('dados.csv', newline='', encoding='UTF-8') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

# Arquivo .csv com a função open()
dados = {'nome':'Ana', 'idade':32, 'enderecos':['a','b']}
with open('dados.json', 'w', encoding='UTF-8') as f:
    json.dump(dados,f)

with open('dados.json', 'r', encoding='UTF-8') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)