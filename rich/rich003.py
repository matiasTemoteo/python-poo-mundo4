from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", justify="left", style="white", no_wrap=True)
tabela.add_column("Preço")

tabela.add_row("Lápis", "[blue]R$ 1,50[/]")
tabela.add_row("Borracha", "[green]R$ 5,00[/]")

print(tabela)
