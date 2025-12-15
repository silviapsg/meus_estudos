from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Spoleto', 'Italiana')
restaurante2 = Restaurante('Burguer King', 'Fast Food')
restaurante3 = Restaurante('China in Box', 'Chinesa')

restaurante2.alternar_estado()

restaurante2.receber_avaliacao('Ana', 4)
restaurante2.receber_avaliacao('João', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()