# Crie classes capazes de calcular fretes de
# veículos diferentes.
#
# Transporte (abstract)
#  + distancia
#  + frete
#  + calc_frete() {abstract}
#
# Moto               Caminhão           Drone
#  + fator = 0.50     + fator = 1.20     + fator = 9.50
#  + calc_frete()     + calc_frete()     + calc_frete()
#
#  (Frete free)       (Min 50km)         (Max 10km)

from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distance):
        self.distance = distance
        self.frete = 0

    def get_frete(self):
        return f"R$ {self.frete:.2f}"

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5

    def calc_frete(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        self.frete = self.fator * self.distance
        return self.get_frete()


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        if self.distance > 50:
            self.frete = self.fator * self.distance
            return self.get_frete()
        else:
            return "Sem entrega! Raio mínimo de 50km"


class Drone(Transporte):
    fator = 9.5

    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        if self.distance < 10:
            self.frete = self.fator * self.distance
            return self.get_frete()
        else:
            return "Sem entrega! Raio máximo de 10km"