# Sistema de frete
from rich import print
from classes_transportes import *
from rich.table import Table

def main():
    dist = 80
    #Primeira maneira de mostrar os dados
    """entrega1 = Drone(dist)
       print(f'Frete de {type(entrega1).__name__} em {dist}Km = {entrega1.calc_frete()}')

        entrega2 = Moto(dist)
        print(f'Frete de {type(entrega2).__name__} em {dist}Km = {entrega2.calc_frete()}')

        entrega3 = Caminhao(dist)
        print(f'Frete de {type(entrega3).__name__} em {dist}Km = {entrega3.calc_frete()}')"""

    #Segunda maneira usando Table
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title= 'Tabela de Fretes')
    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for item in viagem:
        tabela.add_row(f'{dist}Km', f'{type(item).__name__}', f'{item.calc_frete()}')

    print(tabela)

if __name__ == '__main__':
    main()