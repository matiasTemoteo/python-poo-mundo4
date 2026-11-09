import hashlib

class Credencial:
    def __init__(self):
        self.__hash = ""

    @property
    def senha(self) -> str:
        return self.__hash

    @senha.setter
    def senha(self, senha: str):
        if len(senha) > 0:
            hash_ = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            self.__hash = hash_
        else:
            raise ValueError("Senha Inválida!")

    def validar(self, chave):
        senha_u = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if senha_u == self.__hash:
            return True
        else:
            print("Senha incorreta!")
            return False
