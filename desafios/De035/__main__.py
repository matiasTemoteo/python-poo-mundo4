from Classes import *


def main():
    a1 = DOC("prova", 250_000)
    a2 = PDF("Contrato", 1_300_000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)


if __name__ == "__main__":
    main()
