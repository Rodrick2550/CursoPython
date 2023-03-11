class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None


class Coche(Vehiculo):
     Velocidad = ()
     Cilindros = ()

     def __init__(self) :
          self.Velocidad = 10
          self.Cilindros = 8
          self.Color = 'Rojo'
          self.Puertas = 2
          self.Ruedas = 4
          

      
    

coche = Coche()
print(coche.Velocidad)
print(coche.Cilindros)
print(coche.Color)
print(coche.Puertas)
print(coche.Ruedas)