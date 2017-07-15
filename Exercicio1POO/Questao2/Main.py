from Exercicio1POO.Questao2.Produto import Produto
from Exercicio1POO.Questao2.Vendedor import Vendedor


def main():
    vendedor = Vendedor("Caolho", 54, "Masculino", 1500, 153, 803.5, [
        Produto("Notebook", 2000),
        Produto("Computador", 1500),
        Produto("Mouse", 60),
        Produto("Teclado", 120)])

    print(vendedor)

    print("INSS: " + str(vendedor.calcularINSS0()))

if (__name__ == "__main__"):
    main()