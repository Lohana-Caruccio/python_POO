from rich import print
from classes_funcionarios import *


def main ():

    f1 = FuncionarioMensalista('Maria', 2600)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = FuncionarioHorista('João', 45, 220)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == '__main__':
    main()
