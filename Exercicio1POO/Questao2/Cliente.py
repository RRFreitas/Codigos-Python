from Exercicio1POO.Questao2.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__ (self, nome, idade, genero, nascimento):
        super(Cliente, self).__init__(nome, idade, genero)
        self.nascimento = nascimento
