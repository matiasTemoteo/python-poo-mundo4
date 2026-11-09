# Crie a classe Caneta, que simula o funcionamento
# de uma caneta colorida, podendo escrever frases na
# cor relativa

from rich import print
from rich.panel import Panel

class Caneta:

    cores_dict = {
        "azul": "[blue]",
        "verde": "[green]",
        "amarelo": "[yellow]",
        "vermelho": "[red]",
        "roxo": "[purple]",
        "branco": "[white]"
    }

    def __init__(self, cor = "azul"):
        self.cor = self.cores_dict[cor]
        if not self.cor:
            self.cor = "white"

        self.tampada = True

    def destampar(self):
        if self.tampada:
            self.tampada = False
        else:
            print("A caneta já esta destampada!")

    def escrever(self, texto):
        if self.tampada:
            print(f"A caneta {self.cor} esta tampada!")
        else:
            print(f"{self.cor}{texto}[/]", end="")

    def quebrar_linha(self, qnt):
        if self.tampada:
            print(f"A caneta {self.cor} esta tampada!")
        else:
            for i in range(1, qnt):
                print("\n")


c1 = Caneta("vermelho")
c2 = Caneta("azul")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá Gafanhoto!")
c3.escrever("Vamos Exercítar?")
