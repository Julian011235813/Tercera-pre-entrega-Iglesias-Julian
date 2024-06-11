class Vehiculopadre:
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    print(f'Se creo {self}')
  def arrancar(self):
    print(f'el vehiculo {type(self).__name__} arranca')
  def frenar(self):
    print('el vehiculo frena')
    
class Lanchahijo(Vehiculopadre):
  def __init__(self, marca, modelo, motor): 
    self.motor = motor
    super().__init__(marca, modelo) 

vehiculo = Vehiculopadre('Ford', 'Fiesta', 'Rojo')
lancha = Lanchahijo('Yamaha', 'xaquax', 'aquav8')
print(lancha.motor)


#---------------------------------------------------------------------------------------------



