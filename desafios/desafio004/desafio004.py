# Validação de Limite de Páginas
from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_Atual = 1
        print(f'📖 Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem {self.paginas} páginas no total. [yellow]Você agora está na página {self.pagina_Atual}.[/]\n')


    def avancar_paginas(self, quant_P = 1):
        cont = 0
        for pg in range(0, quant_P, 1):
            if not self.fim_do_livro():
                self.pagina_Atual += 1
                print(f'Pág{self.pagina_Atual} ▶️', end=' ')
                sleep(0.2)
                cont += 1
        print(f'Você avançou [purple]{cont} páginas[/], agora está na [purple]página {self.pagina_Atual}.[/]')
        if self.fim_do_livro():
            print(f'\n[red]📕 Você chegou ao final do livro [blue]"{self.titulo}".[/][/]')

    def fim_do_livro(self):
        if self.pagina_Atual == self.paginas:
            return True
        else:
            return False

l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(16)

