from Classes import *


def main():
    p1 = Produto("Mouse", 200)
    p2 = Produto("Teclado", 425)
    p3 = Produto("Laptop", 1750)
    print(p1)
    print(p2)
    print(p3)

    c1 = Carrinho()
    c2 = Carrinho()
    c3 = Carrinho()
    print(c1)
    print(c2)
    print(c3)

    c1 += p1
    c2 += p2
    c1 += c2
    c3 += p3
    c3 += c1

    print(c1)
    print(c2)
    print(c3)


if __name__ == '__main__':
    main()
