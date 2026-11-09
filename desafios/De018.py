# Crie a classe Churrasco, onde seja possível informar
# quantas pessoas vão participar e mostre quanto de carne
# deve ser comprado, o custo total do churrasco e o preço por pessoa

from rich import print
from rich.panel import Panel

class Churrasco:

    qntCarnePorPessoa = 0.4
    custoCarneKg = 82.40

    def __init__(self, titulo,  totalPessoas):
        self.titulo = titulo
        self.totalPessoas = totalPessoas

    def calcular(self) -> dict:
        totalKg = (self.totalPessoas * Churrasco.qntCarnePorPessoa)
        custoTotalKg = totalKg * Churrasco.custoCarneKg
        valorPessoa = custoTotalKg / self.totalPessoas
        return {
            "totalKg": totalKg,
            "custoTotalKg": custoTotalKg,
            "valorPessoa": valorPessoa,
        }

    def analisar(self):
        calculo = self.calcular()
        totalKg = calculo["totalKg"]
        custoTotalKg = calculo["custoTotalKg"]
        valorPessoa = calculo["valorPessoa"]

        textoInicial = f'Analisando [green]{self.titulo}[/] com [blue]{self.totalPessoas} convidados [/]'
        textoConstantes = f'Cada participante comerá [yellow]{Churrasco.qntCarnePorPessoa}Kg [/] e cada Kg custa [yellow] R${Churrasco.custoCarneKg} [/]'
        textoTotalCarne = f'Recomendo comprar [magenta] {totalKg:,.2f}Kg [/] de carne'
        textoTotalCusto = f'O custo total será de [magenta] R${custoTotalKg:,.2f} [/]'
        textoValorPorPessoa = f'Cada pessoa pagará [red] R${valorPessoa:,.2f} [/] para participar'

        textoPainel = f'{textoInicial}\n {textoConstantes}\n {textoTotalCarne}\n {textoTotalCusto}\n {textoValorPorPessoa}'

        self.mostrar_painel(self.titulo, textoPainel)


    def mostrar_painel(self, titulo, texto):
        painel = Panel(f"[white]{texto}[/]", title=f"{titulo}", style="white", width=70)
        print(painel)


c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()
