from modelos.restaurante import Restaurante

restaurante_los_chicos = Restaurante('los chicos', 'mexicana')
restaurante_los_chicos.alternando_estado_do_restaurante()

restaurante_los_chicos.receber_avaliacao('Guilherme', 10)
restaurante_los_chicos.receber_avaliacao('Maria', 8)
restaurante_los_chicos.receber_avaliacao('Luis', 9)





def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()