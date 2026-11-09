# Simule uma cafeteira orientada a objetos
#
# BebidaQuente (abstract)
#  + preparar()
#  + ferver_agua()
#  + misturar() {abstract}
#  + servir() {abstract}
#
# Cafe             Cha             Leite
#  + misturar()     + misturar()    + misturar()
#  + servir()       + servir()      + servir()

from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")

    def ferver_agua(self):
        print("1. Fervendo água a 100ºC.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Adicionar café coado à uma xícara pequena.")


class Cha(BebidaQuente):

    def misturar(self):
        print("2. Mergulhar o sachê de ervas na água fervente.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")


class Leite(BebidaQuente):

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico de leite.")

    def servir(self):
        print("3. Servindo na caneca grande já com café.")