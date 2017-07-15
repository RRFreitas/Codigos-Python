class Produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return "Produto[Nome: " + self.nome + ", Valor: " + str(self.valor) + "]"