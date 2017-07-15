from Exercicio1POO.Questao2.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__ (self, nome, idade, genero, salario, matricula):
        super(Funcionario, self).__init__(nome, idade, genero)
        self.salario = salario
        self.matricula = matricula

    def calcularINSS0(self):
        return self.salario * 0.11