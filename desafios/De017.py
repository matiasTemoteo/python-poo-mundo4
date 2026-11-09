# Crie a classe Produto, onde podemos cadastrar:
# nome, preço.
# Crie também um método que mostre uma etiqueta de preço
# do produto.

from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_etiqueta(self):
        conteudo = f'{self.nome.center(30, " ")}'
        precof = f"{self.preco:,.2f}"
        conteudo += f"{'-' * 30}"
        conteudo += f'{precof.center(30, ".")}'
        print(self.create_panel('Produto', f"[white]{conteudo}[/]"))

    def create_panel(self, title, text):
        return Panel(f'{text}', title=title, style="white", width=35)


p1 = Produto("iphone 14 Pro Max", 25000)
p2 = Produto("Notebook Gamer", 8000)

p1.mostrar_etiqueta()
p2.mostrar_etiqueta()
