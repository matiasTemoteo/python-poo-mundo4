# Simule o sistema de batalha entre personagens
# de um RPG.
#
# Personagem (abstract)
#  + nome
#  + vida
#  + golpes
#  + atacar(alvo, forca)
#  + receber_dano(dano)
#  + curar() {abstract}
#
# Guerreiro       Mago
#  + curar()       + curar()
#

import random
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Personagem(ABC):
    golpes_list = { "fisico": [
        "Pulo Giratório",
        "Gancho de Direita",
        "Gancho de Esquerda",
        "Chute Voador",
        "Agarrão",
        "Soco Forte",
        "Chave de Braço"
    ], "magico": [
        "Choque Mágico",
        "Bola de Fogo",
        "Raio Eletrizante",
        "Vento Cortante",
        "Rajada de Gelo",
        "Raio Mágico",
        "Magia das Sombras"
    ] }

    golpes = []

    def __init__(self, nome, vida, forca_max, tipo):
        self.nome = nome
        self.vida = vida
        self.forca_max = forca_max
        self.golpes = Personagem.golpes_list[tipo]


    def atacar(self, alvo: Personagem, forca):
        if self.vida > 0 and alvo.vida > 0:

            if forca <= self.forca_max:

                dano = self.rolar_dado(forca)

                golpe_usado = random.choice(self.golpes)

                text = f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/])"
                text += f"com um [blue]{golpe_usado}[/] de força [cyan]{forca}[/] "
                text += f"[blue]{alvo.nome}[/] recebeu [red]dano de {dano:.0f}[/]!"
                self.exibir_painel(text, "Combate")

                if dano > 0:
                    alvo.receber_dano(dano)
            else:
                text = "Esse ataque excede a força limite do personagem!!"
                self.exibir_painel(text, "Combate")
        else:
            text = "Algum dos personagens esta fora de combate!!"
            self.exibir_painel(text, "Combate")


    def receber_dano(self, dano):
        if dano <= self.vida:
            self.vida -= dano
        else:
            self.vida = 0


    def rolar_dado(self, valor_base):
        dado = random.randint(1, 20)
        return valor_base * ((dado / 2) / 10)


    def exibir_painel(self, texto, titulo):
        info_panel = Panel(f"{texto}", title=f"{titulo}", style="white", width=60)
        print(info_panel)


    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca_max):
        super().__init__(nome, vida, forca_max, "fisico")
        self.max_vida = vida

    def curar(self):
        pontos_curados = self.rolar_dado(self.max_vida)

        text = f"[blue]{self.nome}[/] usou uma bandagem e [green]recuperou {pontos_curados:.0f} pontos[/] de vida!"
        self.exibir_painel(text, "Curando")


class Mago(Personagem):
    def __init__(self, nome, vida, forca_max):
        super().__init__(nome, vida, forca_max, "magico")
        self.max_vida = vida

    def curar(self):
        pontos_curados = self.rolar_dado(self.max_vida)

        text = f"[blue]{self.nome}[/] usou uma magia de cura e [green]recuperou {pontos_curados:.0f} pontos[/] de vida!"
        self.exibir_painel(text, "Curando")
