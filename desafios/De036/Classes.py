from abc import ABC, abstractmethod
import locale


class Pagamento(ABC):
    def __init__(self):
        self._valor = None


    @property
    def valor(self):
        return self._valor


    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError('Valor inválido!')


    @property
    def fvalor(self) -> str:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True)


    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def __init__(self):
        super().__init__()


    def pagar(self, valor: float):
        try:
            self.valor = float(valor)
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto")
        except Exception as e:
            print(f"Falha no pagamento de ${self.valor} via Boleto!")


class PIX(Pagamento):
    def __init__(self):
        super().__init__()


    def pagar(self, valor: float):
        try:
            self.valor = float(valor)
            print(f"Pagamento CONFIRMADO de {self.fvalor} via PIX")
        except Exception as e:
            print(f"Falha no pagamento de ${self.valor} via PIX!")


class Credito(Pagamento):
    def __init__(self):
        super().__init__()


    def pagar(self, valor: float):
        try:
            self.valor = float(valor)
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Credito")
        except Exception as e:
            print(f"Falha no pagamento de ${self.valor} via Credito!")


def finalizar_compra(pagamento: Pagamento, valor: float):
    try:
        pagamento.pagar(valor)
    except:
        print(f"Não foi possível realizar o pagamento de {pagamento.__class__.__name__}")
