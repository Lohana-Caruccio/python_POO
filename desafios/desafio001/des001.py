# Classe Funcionario
from rich import print
from rich import inspect


class Funcionario:
    # Atributos de Classe
    empresa = '[blue]Curso em Vídeo[/]'

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentaçao(self) -> str:
        return f'🤝 Olá, sou [bold]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'


c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentaçao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentaçao())