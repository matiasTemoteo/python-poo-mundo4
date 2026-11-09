from abc import ABC
import locale


class Funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.__salario = salario


    @property
    def salario(self):
        return self.__salario


    @salario.setter
    def salario(self, novo_salario: float):
        if (novo_salario is None
            or (
                not isinstance(novo_salario, float)
                and not isinstance(novo_salario, int)
            )
        ):
            raise ValueError("Impossível reajustar o salário desse jeito!")
        else:
            if novo_salario < self.__salario:
                raise ValueError("Você não pode reduzir o salário de um funcionário.")
            else:
                self.__salario = novo_salario


    @property
    def salariof(self) -> str:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self.__salario, grouping=True)


    def calcular_bonus(self) -> float:
        bonus = self.__salario * 0.02
        return bonus


    def _montar_str(self, cargo: str, bonus: float) -> str:
        return f"{self.nome} ganha {self.salariof} e por ser {cargo}, o bônus será de {bonus}"


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        bonus = self.salario * 0.15
        return bonus


    def __str__(self):
        return self._montar_str("Gerente", self.calcular_bonus())


class Designer(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        bonus = self.salario * 0.05
        return bonus


    def __str__(self):
        return self._montar_str("Designer", self.calcular_bonus())


class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        bonus = self.salario * 0.10
        return bonus


    def __str__(self):
        return self._montar_str("Desenvolvedor", self.calcular_bonus())
