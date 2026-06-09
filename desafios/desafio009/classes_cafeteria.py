
from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    Emoji = '☕'
    def preparar(self):
        print(f'\n--- {self.Emoji} Iniciando o Preparo {self.Emoji} ---')
        BebidaQuente.ferver_agua(self)
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        print(f'1. Fervendo água a 100 graus Celcius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    Emoji = ' ☕ '
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print(f'3. Servindo uma xícara pequena.')

class Cha(BebidaQuente):
    Emoji = '🍵'
    def misturar(self):
        print(f'2. Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('3. Servindo na caneca de porcelana com limão.')


class Leite(BebidaQuente):
    Emoji = '🥛'
    def misturar(self):
        print(f'2. Passando vapor pressurizado pelo bico de leite')

    def servir(self):
        print(f'3. Servindo na caneca grande, já com café.')