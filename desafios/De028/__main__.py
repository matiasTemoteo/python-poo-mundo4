from Classes import *

def main():
    term = Termostato()

    try:
        term.temperatura = 18.7
    except Exception as e:
        print(f"Houve um problema:\n -> {e}")

    print(f"A temperatura é {term.temperatura}")

if __name__ == '__main__':
    main()
