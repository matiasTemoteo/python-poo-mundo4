from ex008 import *

def main():
    c1 = ContaBacaria(111, "Maria", 5000)
    c1.depositar(100)
    c1.__saldo = 0 # Não acessa o atributo saldo real

    print(c1)

if __name__ == '__main__':
    main()
