
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    a1.aniversario()
    a1.fazer_matricula()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestre')
    p1.dar_aula()

    f1 = Funcionario('Maria', 28, 'Cordenadora', 'Cordenação')
    f1.bater_ponto()

if __name__ == '__main__':
    main()