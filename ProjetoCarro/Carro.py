class Carro():
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
    def acelerar(self):
        print("Carro acelerando")
    def freiar(self):
        print("Carro freiando")
    def __str__(self):
        return "Carro[" + self.modelo + ", " + self.cor + ", " + str(self.ano) + "]"
