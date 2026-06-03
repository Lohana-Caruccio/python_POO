
class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1


class Aluno(Pessoa): # Aluno é subclasse de Pessoa
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de realizar sua matrícula com sucesso!')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'Prof. {self.nome} começou a dar sua aula!')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} acabou de bater seu ponto!')