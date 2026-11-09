# Crie a estrutura capaz de calcular salários
# de funcionários deferentes
#
# Funcionario (abstract)
#  + nome
#  + sal_bruto
#  + salario
#  + sal_min = 1612
#  + inss = 7.5
#  + calc_sal() {abstract}
#  + analisar_sal()
#
# Horista           Mensalista
#  + valor_hora      + calc_sal()
#  + horas_trab
#  + calc_sal()
#

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0


    def sal_pos_inss(self):
        self.salario = self.sal_bruto
        self.salario -= ((self.sal_bruto * self.inss) / 100)


    def analisar_sal(self):
        if self.salario > 0:
            qnt_sal_min = self.salario / self.sal_min
            msg = f"O salário de [blue]{self.nome}[/], ([purple]Funcionário {self.__class__.__name__}[/]) é de "
            msg += f"[green]R$ {self.salario:.2f} [/] e corresponde a [yellow]{qnt_sal_min:.2f} sslários mínimos[/]"
            infoPanel = Panel(f"{msg}", title=f"Análise de Salário", style="white", width=50)
            print(infoPanel)
        else:
            print("Must calculate Salario first!")


    @abstractmethod
    def calc_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, hrs_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.hrs_trab = hrs_trab


    def calc_sal(self) -> str:
        self.sal_bruto = self.valor_hora * self.hrs_trab
        self.sal_pos_inss()
        return f"Salario: R$ {self.salario:.2f}"


class Mensalista(Funcionario):
    def __init__(self, nome, sal):
        super().__init__(nome)
        self.sal_bruto = sal


    def calc_sal(self) -> str:
        self.sal_pos_inss()
        return f"Salario: R$ {self.salario:.2f}"
