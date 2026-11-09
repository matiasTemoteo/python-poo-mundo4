from rich import print, inspect

from classes import Aluno, Professor, Funcionario


def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    # inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestre')
    p1.fazer_aniversario()
    p1.dar_aular()
    # inspect(p1, methods=True)

    f1 = Funcionario('Fernando', 28, 'Especialista Contábil', 'Administrativo')
    f1.fazer_aniversario()
    f1.bater_ponto()
    # inspect(f1, methods=True)

if __name__ == '__main__':
    main()

