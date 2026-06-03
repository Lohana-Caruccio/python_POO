from rich import print, inspect
from classesEx005 import Aluno, Professor, Funcionario

a1 = Aluno('José', 17, 'Informática', 'T01')
a1.aniversario()
a1.fazer_matricula()

p1 = Professor('Samuel', 37, 'Biologia', 'Mestre')
p1.dar_aula()

f1 = Funcionario('Maria', 28, 'Cordenadora', 'Cordenação')
f1.bater_ponto()