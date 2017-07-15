from Exercicio1POO.Questao3.Funcionario import Funcionario
from Exercicio1POO.Questao3.Fornecedor import Fornecedor


def main():
    fornecedor = Fornecedor("Google inc", "New York", 666666, 1000, 50)

    print("Saldo do fornecedor " + fornecedor.nome + ": " + str(fornecedor.obterSaldo()))
    print()

    funcionario = Funcionario("Jubileu", "Fernando de Noronha", 777777, 7, 7000, 700)
    print("Salário total do funcionário " + funcionario.nome + ": " + str(funcionario.calcularSalarioTotal()))

if(__name__ == "__main__"):
    main()