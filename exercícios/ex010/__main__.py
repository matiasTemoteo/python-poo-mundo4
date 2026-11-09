from ex010 import*
from rich import inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.nota = 7
    print(f"{av1.nome} tirou nota {av1.nota} em {av1.disciplina}")
    inspect(av1, private=True)

if __name__ == "__main__":
    main()
