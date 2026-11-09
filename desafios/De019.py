# Crie uma classe Livro, que vai simular a passagem
# de páginas de um livro.
# Considerando também se o usuário chegou ao fim da leitura

from rich import print

class Livro:

    paginaAtual = 1

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

        print(f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} páginas no total. Você está na página 1.")
        print(f"{'-' * 75}")

    def avancar_paginas(self, qntPaginas):

        for pag in range(0, qntPaginas):
            if self.paginaAtual < self.paginas:
                self.paginaAtual += 1
                print(f':arrow_forward: Pág_[blue]{self.paginaAtual}[/] ', end="")
                if pag == qntPaginas - 1:
                    print(f"Você avançou {qntPaginas} páginas e agora esta na [blue]página {self.paginaAtual}[/]")
            else:
                print(f"\nVocê chegou ao final do livro '{self.titulo}'")
                break


l1 = Livro("10 coisas que aprendi", 31)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(8)
l1.avancar_paginas(8)
