from Classes import *


def main():
    c1 = Carteira(160)
    c2 = Carteira(200)

    c1 += 50
    c1 -= 10

    if c1 == c2:
        print("Vocês tem o mesmo valor na carteira")
    else:
        print("As carteiras tem valores diferentes")

    print(c1)


if __name__ == '__main__':
    main()
