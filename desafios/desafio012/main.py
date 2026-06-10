# Jogo de RPG

from classes_personagens import *


def main():
    p1 = Guerreiro('Kratos', 3000)
    p2 = Mago('Gandalf', 2000)
    p1.atacar(p2, 200)
    p2.atacar(p1, 200)
    p1.curar()
    p2.curar()




if __name__ == '__main__':
    main()