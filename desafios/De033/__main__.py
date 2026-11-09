from Classes import *


def main():
    a = Aluno("Matheus", 1994, "ADM")
    b = Aluno("Carlos", 1997, "ADS")

    a.nascimento = 1995

    a.add_curso("ALL")
    b.curso = "ALL"

    print(a.__dict__, f"Idade: {a.idade}")
    print(b.__dict__, f"Idade: {b.idade}")

if __name__ == '__main__':
    main()
