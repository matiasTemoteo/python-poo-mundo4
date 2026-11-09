class Diario:
    def __init__(self, senha = "1414@1"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, mensagem):
        if (isinstance(mensagem, str) and
        len(mensagem.strip()) > 0):
            self.__segredos.append(mensagem)
        else:
            return False

    def ler(self, senha = None):
        if senha == self.__senha:
            print("Diário LIBERADO")
            for seg in enumerate(self.__segredos):
                print(f" - {seg[1]}")
        else:
            raise PermissionError("Senha incorreta! Você não pode ler o diário")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, nSenha):
        if isinstance(nSenha, str) and len(nSenha.strip()) > 0:
            self.__senha = nSenha.strip()
        else:
            raise Exception("Padrão de Senha não aceito!")
