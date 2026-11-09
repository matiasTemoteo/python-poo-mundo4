from Classes import *

def main():
    diario = Diario()
    diario.escrever("Primeira mensagem")
    diario.escrever("Segunda mensagem")

    try:
        diario.senha = "22$221"
    except Exception as e:
        print(e)

    try:
        diario.ler("22$221")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
