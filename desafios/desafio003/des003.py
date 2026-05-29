# Sistema de Análise de Churrasco
from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de classe
    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo, quant):
       # Atributos de instância
        self.titulo = titulo
        self.quant = quant

    def calcular_qtd_carne(self):
        return self.quant * self.consumo_padrao

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_preco_individual(self):
        return self.calcular_custo_total() / self.quant

    def analisar(self):

        conteudo = f'Analisando [green]{self.titulo}[/] com [green]{self.quant} convidados[/]'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:.2f}'
        conteudo += f'\nRecomendo comprar [blue]{self.calcular_qtd_carne()}Kg[/] de carne'
        conteudo += f'\nO custo total será de [yellow]R${self.calcular_custo_total():.2f}[/]'
        conteudo += f'\nCada pessoa pagará [yellow]R${self.calcular_preco_individual():.2f}[/] para participar'

        etiqueta = Panel(conteudo, title= f'{self.titulo}')
        return etiqueta


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())

c2 = Churrasco('Churrasco da Família', 5)
print(c2.analisar())

