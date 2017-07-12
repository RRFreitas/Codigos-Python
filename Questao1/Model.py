class Animal():
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover(self):
        print("Animal se move de forma genérica")

    def comunicar(self):
        print("Animal se comunica de forma genérica")

    def __str__(self):
        return "Nome: %s, peso: %d, habitat: %s" % (self.nome, self.peso, self.habitat)


class Cachorro(Animal):
    def __init__(self,nome, peso, habitat, raca):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat
        self.raca = raca

    def brincar(self):
        print("Cachorro brincando!")

    def vigiar(self):
        print("Cachorro vigiando!")
    def __str__ (self):
        return "nome: %s, peso: %d, habitat: %s, raca: %s" % (self.nome, self.peso, self.habitat, self.raca)

class Peixe(Animal):
    def __init__(self, nome, peso, habitat, tipoCauda):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat
        self.cauda = Cauda(tipoCauda)
    def __str__ (self):
        return "nome: %s, peso: %d, habitat: %s, cauda: %s" % (self.nome, self.peso, self.habitat, self.cauda)

class Cauda():
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__ (self):
        return "TipoCauda: %s" % (self.tipo)
