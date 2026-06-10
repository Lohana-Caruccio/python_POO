#Cálculo de salário
from rich import print
from abc import ABC, abstractmethod
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome= None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0


    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        analise = self.salario / Funcionario.sal_min
        painel = Panel(f'O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) é de '
                       f'[green]R${self.salario:.2f}[/] e corresponde a [yellow]{analise:.1f}[/] salários mínimos.', title='Análise de Salário', width=50)
        print(painel)


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto= Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto


    def calc_sal(self):
        desconto = (self.sal_bruto * Funcionario.inss)/100
        self.salario = self.sal_bruto - desconto
        return self.salario


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trabalhadas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas



    def calc_sal(self):
        deconto = (self.sal_bruto * Funcionario.inss)/100
        self.salario = self.sal_bruto - deconto
        return self.salario
