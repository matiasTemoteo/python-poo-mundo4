from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, nome: str = ""):
        self.nome = nome


    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e esta emitindo som")


class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} disse 'quack quack'!")


class Cachorro(Animal):

    def emitir_som(self):
        print(f"{self.nome} disse 'Au Au Au'!")


class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} disse 'au!au!au!au!'!")


class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} disse 'ruf ruf ruf'!")


class Gato(Animal):

    def emitir_som(self):
        print(f"{self.nome} disse 'miau miau'!")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} disse 'Po Po Po'!")


