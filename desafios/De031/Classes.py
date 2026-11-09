
class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    def calc_area(self):
        self._area = self._base * self._altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, int) and not isinstance(base, float):
            raise TypeError("O valor da base deve ser um número!")
        elif base < 0:
            raise ValueError("Valor invalido para a base!")
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, int) and not isinstance(altura, float):
            raise TypeError("O valor da base deve ser um número!")
        elif altura < 0:
            raise ValueError("Valor invalido para a base!")
        else:
            self._altura = altura

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("Área não pode ser configurada!")

    @property
    def medidas(self):
        return f"Base: {self._base:.2f}\nAltura: {self._altura:.2f}\nArea: {self.area:.2f}"

    @medidas.setter
    def medidas(self, medidas:tuple):
       if not isinstance(medidas, tuple):
           raise TypeError("As medidas dever ser informadas dentro de uma tupla!")
       if len(medidas) != 2:
           raise SyntaxError("Informe uma tupla com 2 valores numéricos!")
       if isinstance(medidas[0], float) or isinstance(medidas[0], int):
           self.base = medidas[0]
       else:
           raise TypeError("A base deve ser um número!")
       if isinstance(medidas[1], float) or isinstance(medidas[1], int):
           self.altura = medidas[1]
       else:
           raise TypeError("A altura deve ser um número!")

