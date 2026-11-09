from Classes import *


def main():
    funcionarios = [
        Gerente("Matheus", 9850),
        Designer("Lucas", 3780),
        Desenvolvedor("Marcos", 5900)
    ]

    funcionarios[1].salario = 3950

    for funcionario in funcionarios:
        print(funcionario)


if __name__ == "__main__":
    main()
