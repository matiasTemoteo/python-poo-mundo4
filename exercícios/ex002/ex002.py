# Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar um novo Gafanhoto, use: variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafonhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

# Declaração de Objetos

g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)
print(g1.__doc__) # "__doc__" -> Dunder Atribute
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2)
print(g2.__doc__)
print(g2.__dict__)
print(g2.__getstate__())
print(g2.__class__)

g3 = Gafanhoto("Alan", 25)
g3.aniversario()
print(g3)
print(g3.__doc__)
print(g3.__dict__)
print(g3.__getstate__())
print(g3.__class__)