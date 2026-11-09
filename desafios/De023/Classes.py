# Implemente o seguinte diagrama de classes

#  Poligono (abstract)
#   + qtd_lados
#   + perimetro() {abstract}
#   + area() {abstract}

#  Quadrado                Circulo
#   + lado                  + raio
#   + perimetro()           + perimetro()
#   + area()                + area()


from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):
    def __init__(self, qtd_lados: int):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado: int = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> str:
        per = self.lado * self.qtd_lados
        return f"{per:.1f}"

    def area(self) -> str:
        area = self.lado ** 2
        return f"{area:.1f}"


class Circulo(Poligono):
    def __init__(self, raio: int = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> str:
        per = self.raio * (2 * pi)
        return f"{per:.1f}"

    def area(self) -> str:
        area = pi * (self.raio ** 2)
        return f"{area:.1f}"
