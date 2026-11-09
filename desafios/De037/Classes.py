from rich import print
from rich.panel import Panel


class Mensagem:
    def __init__(self, msg: str = "", tipo: str = "aviso", icone: str = "speech_balloon"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone


    def definir_painel(self, style: str = ""):
        msg_icone = f":{self._icone}:"
        msg_title = f"{msg_icone} {self._tipo.upper()} {msg_icone}"

        return Panel(
                f'\n[white]{self._mensagem}[/]\n',
                title=f'{msg_title}',
                style=f'{style}',
                width=50
            )


    def mostrar(self):

        print(
            self.definir_painel("#dddddd")
        )


class Aviso(Mensagem):
    def __init__(self, msg: str):
        super().__init__(msg, "aviso", "warning")


    def mostrar(self):

        print(
            self.definir_painel("#000000 on #fffc1b")
        )


class Erro(Mensagem):
    def __init__(self, msg: str):
        super().__init__(msg, "Erro", "prohibited")


    def mostrar(self):

        print(
            self.definir_painel("#fff000 on #880000")
        )
