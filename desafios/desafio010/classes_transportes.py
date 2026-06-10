
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator :float = 0.50

    def calc_frete(self):
        return f'[yellow]R${Moto.fator * self.distancia:.2f}[/]'


class Caminhao(Transporte):
    fator :float = 1.20

    def calc_frete(self):
        if self.distancia >= 50:
            return f'[yellow]R${Caminhao.fator * self.distancia:.2f}[/]'
        else:
            return f'[yellow]Raio mínimo de 50Km[/]'


class Drone(Transporte):
    fator :float = 9.50

    def calc_frete(self):
        if self.distancia <= 10:
            return f'[yellow]R${Drone.fator * self.distancia:.2f}[/]'
        else:
            return f'[yellow]Raio máximo de 10Km[/]'