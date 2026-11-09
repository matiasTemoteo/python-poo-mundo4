from Classes import *

def main():
    guerreiro = Guerreiro("Kratos", 2000, 2000)
    mago = Mago("Merlin", 1800, 2000)

    guerreiro.atacar(mago, 1500)
    mago.atacar(guerreiro, 1900)
    guerreiro.curar()
    mago.atacar(guerreiro, 1900)
    mago.curar()
    guerreiro.atacar(mago, 1500)

if __name__ == '__main__':
    main()
