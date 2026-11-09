#Crie a classe Funcionário, onde podemos cadastrar:
# nome, setor e cargo.
#
# Crie também um método que permita ao funcionário se
# apresentar

from rich import print
from rich import inspect

class Funcionário:

    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return (f'Olá, meu nome é [blue]{self.nome}[/], atuo no setor de {self.setor} da emppresa {self.empresa} como {self.cargo}.')



c1 = Funcionário("Maria", "Administração", "Diretora")
print(c1.apresentar())

c2 = Funcionário("Pedro", "TI", "Programador")
print(c2.apresentar())


# inspect(c1, methods=True)
