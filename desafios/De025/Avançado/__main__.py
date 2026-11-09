from Classes import *
from rich import print
from rich.table import Table


def main():
    distancia = 5
    peso = 25

    viagem = [
        Moto(peso, distancia),
        Caminhao(peso, distancia),
        Drone(peso, distancia)
    ]

    table = Table(title="Tabela de Fretes")

    table.add_column("Distância")
    table.add_column("Tipo")
    table.add_column("Frete")

    for veiculo in viagem:
        table.add_row(
            f"{distancia} km",
            f"{veiculo.__class__.__name__}",
            f"{veiculo.calc_frete()}"
        )

    print(table)

if __name__ == "__main__":
    main()
