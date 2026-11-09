from Classes import *
from rich import inspect

def main():
    c = Credencial()
    c.senha = str(input("Insira sua senha: "))
    print(c.senha)

    senha_u = str(input("Insira a senha a ser verificada: "))
    c.validar(senha_u)

if __name__ == "__main__":
    main()
