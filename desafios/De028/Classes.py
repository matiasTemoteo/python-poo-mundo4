class Termostato:
    def __init__(self):
        self.__temperatura = 22

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @property
    def ftemperatura(self) -> str:
        return f"{self.__temperatura} °C"

    @temperatura.setter
    def temperatura(self, temp: float):
        if (temp % 0.5 != 0):
            raise ValueError(f"Temperatura de {temp} é inválida!")

        self.__temperatura = min(max(temp, 16), 30)
