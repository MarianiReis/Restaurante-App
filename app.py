from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praça = Restaurante('Praça', 'Padaria')
pao_frances = Prato('Pão Francês', 1.00, 'Pão Frances Fermentação Natural')
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Médio')
restaurante_praça.adicionar_item_cardapio(pao_frances)
restaurante_praça.adicionar_item_cardapio(bebida_suco)


def main():
    restaurante_praça.exibir_cardapio

if __name__ == '__main__':
    main()