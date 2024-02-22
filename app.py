from modelos.restaurante import Restaurante

restaurante_los_chicos = Restaurante('los chicos', 'mexicana')
restaurante_los_chicos.alternando_estado_do_restaurante()


def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
