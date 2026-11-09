from Classes import *
from rich import inspect

def main():
    rect = Retangulo(4, 5)

    try:
        rect.base = 3
        rect.altura = 3

        rect.medidas = (4, 5)

        print(rect.medidas)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
