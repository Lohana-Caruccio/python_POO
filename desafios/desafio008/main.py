# Cálculo Área e Perímetro de Polígonos
from rich import print
from classes import *

def main ():
    p1 = Quadrado(20)
    print(f'[bold][blue]QUADRADO[/]')
    print(f'Perímetro: {p1.perimetro():.1f} m')
    print(f'Area: {p1.area():.1f} m2')

    p2 = Circulo(20)
    print('\n[bold][blue]CÍRCULO[/]')
    print(f'Perímetro: {p2.perimetro():.1f} m')
    print(f'Area: {p2.area():.1f} m2')


if __name__ == '__main__':
    main()
