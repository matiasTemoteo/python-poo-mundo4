class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Métodos acessores
    def get_nota(self) -> float: # Getter
        return self._nota

    def set_nota(self, nota: float): # Setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida!")
