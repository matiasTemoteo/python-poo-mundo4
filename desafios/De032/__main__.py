from Classes import *


def main():
    cc = ContaBancaria(111, "Jose", 10000, "778458")

    print("-> Sacando 500...")
    cc.sacar(500)

    print("-> Depositando 752...")
    cc.depositar(752)

    print("-> Sacando 800...")
    cc.sacar(800)

    print("Mudando de nome...")
    cc.nome = str(input("-> Nome: "))

    print(cc)

if __name__ == '__main__':
    main()
