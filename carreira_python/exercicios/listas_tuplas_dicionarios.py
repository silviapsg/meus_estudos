'''
Características da LISTA:
- Ordenada;
- Mutável.
'''

# Lista vazia
lista = []
print(lista)

# Lista com valores atribuídos
lista = [1, "Python", 2]
print(lista)

# Acessar um valor da lista
lista[0] 
print(lista[0])

# Alterar um valor da lista
lista[0] = "VS Code"
print(lista)

# Adicionar um novo valor na lista
lista.append("Novo")
print(lista)

lista.insert(0, "Aleatório")
print(lista)

# Criar uma lista com filmes
filmes = ["O Senhor dos Anéis: O Retorno do Rei", "Harry Potter e as Relíquias da Morte", "Divertida Mente 2" ]
print(filmes)

'''
Características da TUPLA:
- Ordenada;
- Imutável.
'''

# Tupla com valores atribuídos
tupla = 123, 345, "Olá"
print(tupla)

# Acessar um valor da tupla
tupla[2]
print(tupla[2])

# Tupla com outra tupla e lista
tupla_mista = tupla, lista
print(tupla_mista)

# Criar um tupla com datas
datas = "15/08/2004", "22/11/2013", "10/06/2021"
print(datas)

'''
Características do DICIONÁRIO:
- Não ordenado;
- Mutável;
- Chave: valor.
'''

# Declarar um dicionário
telefones = {"João": 91128394, "Leo": 92234195}
print(telefones)

# Acessar o valor de uma chave em um dicionário
telefones["João"]
print(telefones["João"], telefones["Leo"])

# Adicionar um novo valor ao dicionário
telefones["Helena"] = 95461789
print(telefones)

# Criar um dicionário onde a chave é o nome do filme e o valor é a data
filmes_datas = {}
filmes_datas[filmes[0]] = datas[0]
filmes_datas[filmes[1]] = datas[1]
filmes_datas[filmes[2]] = datas[2]
print(filmes_datas)

for i in lista:
    print(i)

for i in tupla:
    print(i)

for chave, valor in filmes_datas.items():
    print(chave, valor)