from Classes import *


def main():
    x = Analisador()
    x.analisar(2)
    x.analisar("i")
    x.analisar("8.5")
    x.analisar(8.5)
    x.analisar(["a", "b", "c"])
    x.analisar({"a": 1, "b": 2})
    x.analisar((1, 4, 5))
    x.analisar(max([5, 9 , 8]))
    x.analisar(len([1, 5, 6]))


if __name__ == '__main__':
    main()
