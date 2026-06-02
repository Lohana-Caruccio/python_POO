# CANETA que escreve colorido
from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        self.cor = cor.upper().lower()
        self.tampada = True


    def destampar(self):
       self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, txt):
        corT = self.traduzir(self.cor)
        if self.tampada:
            print(f'\n⛔  Sua [{corT}]caneta[/] está tampada!')
        else:
            print(f'[{corT}]{txt}[/]', end= ' ')

    def quebra_linha(self, qtd = 1):
        print ('\n' * qtd)

    def traduzir(self, cor):
        if cor == 'azul':
            cor = 'blue'
        elif cor == 'vermelho':
            cor = 'red'
        elif cor == 'verde':
            cor = 'green'
        elif cor == 'amarelo':
            cor = 'yellow'
        elif cor == 'roxo':
            cor = 'purple'
        else:
            cor = 'white'
        return cor


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('roxo')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebra_linha(2)
c2.escrever('Olá Gafanhoto!')
c2.quebra_linha(3)
c3.escrever('Vamos exercitar...')
