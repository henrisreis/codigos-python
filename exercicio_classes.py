# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

ford_ka = Carro('Ford Ka')
motor_1_0 = Motor('1.0')
ford = Fabricante('Ford')

ford_ka.fabricante = ford
ford_ka.motor = motor_1_0

print(ford_ka.nome, ford_ka.motor.nome, ford_ka.fabricante.nome)

celta = Carro('Celta')
chevrolet = Fabricante('Chevrolet')

celta.motor = motor_1_0
celta.fabricante = chevrolet

print(celta.nome, celta.motor.nome, celta.fabricante.nome)