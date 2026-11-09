# Crie a classe Gamer, onde podemos cadastrar
# nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a
# ficha desse gamer


from rich import print
from rich.panel import Panel


class Gamer:

    jogos = []

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, titulo):
        if titulo not in self.jogos:
            self.jogos.append(titulo)
            print(self.jogos[0])
            self.jogos = sorted(self.jogos, key=str.lower)
        else:
            print(f"O jogo '{titulo}' já consta na lista de favoritos!")

    def ficha(self):
        jogosText = ""
        for jogo in self.jogos:
            jogosText += jogo + "\n"

        panelText = f"Nome real: [black on blue] {self.nome} [/]\n\nJogos Favoritos:\n\n[blue]{jogosText}[/]"

        fichaJogos = Panel(f"[white]{panelText}[/]", title=f"<{self.nick}>", style="white", width=70)
        print(fichaJogos)


j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()
