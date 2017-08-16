class Pessoa():
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        print("Falando de forma genérica")
    def andar(self):
        print("Andando de forma genérica")
    def pagar(self):
        print("Pagando de forma genérica")

class Cliente(Pessoa):
    def __init__(self, nome):
        super(Cliente, self).__init__(nome)
    def pagar(self):
        print("Pagando como cliente")

class Funcionario(Pessoa):
    def __init__(self, nome):
        super(Funcionario, self).__init__(nome)

class Maratona():
    def correr(self, pessoa):
        pessoa.andar()
        pessoa.falar()



