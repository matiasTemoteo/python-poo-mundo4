from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome: str, tamanho: int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho


    @property
    def extensao(self):
        return self._extensao


    @extensao.setter
    def extensao(self, ext: str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo esta em um formato não suportado!")


    @property
    def nome_completo(self):
        tamanho = f"{(self.tamanho / 1000000):.1f}MB"
        return f"'{self.nome}.{self._extensao}({tamanho})'"


    @abstractmethod
    def abrir(self):
        pass


class DOC(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        Arquivo.__init__(self, nome, tamanho)
        self.extensao = 'docx'


    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


class PDF(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        Arquivo.__init__(self, nome, tamanho)
        self.extensao = 'pdf'


    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")


def abrir_arquivo(arquivo: Arquivo):
    try:
        arquivo.abrir()
    except:
        print(f"Não foi possível abrir o arquivo: {arquivo.__class__.__name__}")
