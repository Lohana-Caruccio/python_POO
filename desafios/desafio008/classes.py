from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtdL):
        self.qtd_lados = qtdL

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(qtdL = 4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    pi: float = 3.14
    def __init__(self, raio = 1):
        super().__init__(qtdL = 0)
        self.raio = raio

    def perimetro(self):
        return (2 * Circulo.pi) * self.raio

    def area(self):
        return Circulo.pi * (self.raio ** 2)
