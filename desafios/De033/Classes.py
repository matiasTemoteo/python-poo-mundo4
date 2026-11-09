from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome: str, nasc: int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc


    @property
    def nascimento(self, ano):
        return self._nascimento


    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é invalido!")


    @property
    def idade(self):
        return date.today().year - self._nascimento


    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade! Mude o ano de nascimento!")


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso


    @property
    def curso(self):
        return self._curso


    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"Curso {curso} não esta na lista de cursos oficiais!")


    def add_curso(self, valor):
        valor = valor.strip().upper()

        if valor in self.cursos_oficiais:
            raise ValueError(f"Curso {valor} já esta na lista de cursos oficiais!")
        elif not 3 <= len(valor) <= 5:
            raise ValueError(f"Nome do curso {valor} esta fora do padrão esperado!")
        else:
            Aluno.cursos_oficiais.append(valor)
