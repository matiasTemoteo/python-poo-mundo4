from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de fazer a matricula!")

    def estudar(self):
        print(f'O aluno {self.nome} esta estudando no curso {self.curso} na turma {self.turma}!')


class Professor(Pessoa):
    def __init__(self, nome, idade, epecialidade, nivel):
        super().__init__(nome, idade)
        self.epecialidade = epecialidade
        self.nivel = nivel

    def dar_aular(self):
        print(f"O Professor {self.nome} começou a dar aula!")

    def estudar(self):
        print(f'O Professor {self.nome} esta estudando a {self.epecialidade} no nível {self.nivel}!')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu o ponto!")

    def estudar(self):
        print(f'O funcionário {self.nome} esta estudando os conceitos do cargo {self.cargo} dentro do setor {self.setor}!')
