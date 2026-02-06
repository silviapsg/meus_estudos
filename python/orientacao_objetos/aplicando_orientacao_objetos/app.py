from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Spoleto', 'Italiana')
bebida1 = Bebida('Coca-Cola', 6, 'lata')
bebida1.aplicar_desconto()
prato1 = Prato('Fettuccine À Carbonara', 35.06, '200 g de fettuccine + molho super cremoso à base de creme de leite, ovo, queijo parmesão e pimenta preta + 2 pegadas de bacon adicionados na hora')
prato1.aplicar_desconto()
restaurante1.adicionar_item(bebida1)
restaurante1.adicionar_item(prato1)

def main():
    print(bebida1)
    print(prato1)

if __name__ == '__main__':
    restaurante1.exibir_cardapio