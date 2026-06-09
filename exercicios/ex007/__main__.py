from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    a1.aniversario()
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestre')
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario('Maria', 28, 'Cordenadora', 'Cordenação')
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()

