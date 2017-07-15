from Exercicio1POO.Questao2.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__ (self,  nome, idade, genero, salario, matricula, nomeGerencia):
        super(Gerente, self).__init__(nome, idade, genero, salario, matricula)
        self.nomeGerencia = nomeGerencia