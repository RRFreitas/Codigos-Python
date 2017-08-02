from Carro import Carro
from Hibrido import Hibrido

def main():
    carro1 = Carro("Preto", "Fusca", 2018)
    print(carro1)
    carro1.acelerar()
    carro1.freiar()

if __name__ == "__main__":
    main ()
