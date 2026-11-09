from Classes import *


def main():
    finalizar_compra(Boleto(), 1500)
    finalizar_compra(PIX(), 785)
    finalizar_compra(Credito(), 3650)


if __name__ == '__main__':
    main()
