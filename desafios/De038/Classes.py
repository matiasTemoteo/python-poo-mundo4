from functools import singledispatchmethod
import locale
from typing import List


def formata_dinheiro(valor: float):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor)


class Produto:
    def __init__(self, nome: str, preco: float = 0):
        self.nome = nome
        self.preco = preco


    @property
    def precof(self):
        return formata_dinheiro(self.preco)


    def __str__(self):
        return f"{self.nome} ({self.precof})"


class Carrinho:
    def __init__(self, produtos: List[Produto] = None):
        self.produtos: List[Produto] = produtos if produtos else []


    @property
    def total(self):
        total_valor = sum(p.preco for p in self.produtos)
        return f"Total: {formata_dinheiro(total_valor)}"


    @singledispatchmethod
    def __iadd__(self, carrinho):
        prod_car = carrinho.produtos
        for produto in prod_car:
            self.produtos.append(produto)
        return self


    @__iadd__.register(Produto)
    def _(self, produto: Produto):
        self.produtos.append(produto)
        return self


    def __str__(self):
        str_texto = "\n"
        str_texto += "-" * 9
        str_texto += "Carrinho"
        str_texto += "-" * 9
        for produto in self.produtos:
            str_texto += f"\n{produto.nome} ({produto.precof})"
        str_texto += "\n"
        str_texto += ("-" * 25) + "\n"
        str_texto += self.total + "\n"
        str_texto += "-" * 25
        return str_texto
