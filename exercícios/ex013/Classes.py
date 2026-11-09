
class Mae:
    def __init__(self, nome: str = "Mamãe"):
        self.nome = nome


    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite condensado e calda")


    def fritar_coxinha(self):
        print(f"{self.nome} frita COXINHA no óleo de soja")


class Filho(Mae):
    def __init__(self, nome: str):
        super().__init__(nome)


    def fritar_coxinha(self):
        print(f"{self.nome} frita COXINHA na Air Fryer")


class Filha(Mae):
    def __init__(self, nome: str):
        super().__init__(nome)


    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com Leite Ninho com Nutella")
