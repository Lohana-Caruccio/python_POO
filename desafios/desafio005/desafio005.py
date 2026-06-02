# Classe Gamer para organizar jogos favoritos
from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos, key= str.lower)

    def ficha(self):
        conteudo = f'[bold]Nome Real:[/] [black on blue] {self.nome} [/]'
        conteudo += f'\n[bold]Jogos Favoritos:[/]'
        for j in self.favoritos:
            conteudo += f'\n🎮 [blue]{j}[/]'
        etiqueta = Panel(conteudo, title= f'Jogador [purple]< {self.nick} >[/]', width=40)
        return etiqueta


g1 = Gamer('Maria da Silva', 'detonator001')
g1.add_favoritos('Alice Madness Return')
g1.add_favoritos('Sally Face')
g1.add_favoritos('Little MissFortune')
g1.add_favoritos('Fran Bow')
print(g1.ficha())

g2 = Gamer('Bruno de Oliveira', 'pipipopo')
g2.add_favoritos('Mario Bross')
print(g2.ficha())