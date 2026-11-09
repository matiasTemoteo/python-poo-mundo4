from Classes import *

def main():
    p1 = Quadrado(12)

    print(" ----- Quadrado ----- ")
    print(f"Perimetro = {p1.perimetro()} mm")
    print(f"Área = {p1.area()} mm2")
    print("")

    c1 = Circulo(12)

    print(" ----- Circulo ----- ")
    print(f"Perimetro = {c1.perimetro()} cm")
    print(f"Area = {c1.area()} cm2")
    print("")

if __name__ == "__main__":
    main()
