from Classes import *


def main():
    alunos = [
        Aluno("Gabriel", "ADS", "1"),
        Aluno("Alana", "ADM", "1")
    ]

    usuarios = [
        Usuario("alan123", "alan@mail.com"),
        Usuario("bebe15e", "beatriz_re@gmail.com")
    ]

    exportar_dados(JSON(), alunos)
    exportar_dados(JSON(), usuarios)

    exportar_dados(XML(), alunos)
    exportar_dados(XML(), usuarios)


if __name__ == '__main__':
    main()
