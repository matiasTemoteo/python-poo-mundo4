from ex009 import*
from rich import inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.set_nota(8)
    print(f"{av1.nome} tirou nota {av1.get_nota()} em {av1.disciplina}")
    inspect(av1, private=True)

if __name__ == "__main__":
    main()
