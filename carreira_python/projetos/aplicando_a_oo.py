# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. 
# Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.
# Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):
# nome
# artista
# duracao
# Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo...

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica('Blank Space', 'Taylor Swift', 4)
musica2 = Musica('Que Sorte A Nossa', 'Matheus & Kauan', 3)
musica3 = Musica('Faroeste Caboclo', 'Legião Urbana', 10)

print(f'A música 1 é {musica1.nome} de {musica1.artista} com duração de {musica1.duracao} minutos.')
print(f'A música 2 é {musica2.nome} de {musica2.artista} com duração de {musica2.duracao} minutos.')
print(f'A música 3 é {musica3.nome} de {musica3.artista} com duração de {musica3.duracao} minutos.')

# A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. 
# Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como título, autor e número de páginas:
# class Livro:
#     def __init__(self, titulo='', autor='', paginas=0):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas
#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'
#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'
#     def aumentar_paginas(self, quantidade):
#         self.paginas += quantidade
# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho com {self.profissao}'
        else:
            return f'Olá, sou {self.nome}'
    
    def aniversario(self):
        self.idade +=1

pessoa1 = Pessoa('Ana', 18, 'Estudante')
pessoa2 = Pessoa('José', 32, 'Engenheiro')
pessoa3 = Pessoa('Maria', 54, 'Advogada')
pessoa4 = Pessoa('João', 85, 'Aposentado')

print('\nInformações Iniciais:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa4)
print()

pessoa1.aniversario()
pessoa2.aniversario()
pessoa3.aniversario()
pessoa4.aniversario()

print('Informações após aniversário:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa4)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
print(pessoa4.saudacao)