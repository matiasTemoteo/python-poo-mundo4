class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Criando atributos validáveis
    @property
    def nota(self) -> float: # Getter
        return self._nota

    @nota.setter
    def nota(self, nota: float):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida!")
