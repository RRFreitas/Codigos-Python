from Carro import Carro

class Hibrido(Carro):
    def __init__(self, cor, modelo, ano):
        super(Hibrido, self).__init__(cor, modelo, ano)
    def carregarBateria(self):
        print("Carregando Bateria")
