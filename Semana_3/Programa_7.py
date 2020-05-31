class Coche:
  def __init__(self):
    print("Marca")
    print("Modelo")
    print("Color")
    print("Combustible")
    print("Numero de serie")
  def metodosCoche(self):
    print("Acelerar")
    print("Frenar")
'Subclase 1'
class Deportivo(Coche):
  def __init__(self):
    print("Caballos de fuersa")
    print("Velocidad maxima")
    print("Motor")
    print("Matricula")
    print("Trasmicion")
  def metodosDeportivo(self):
    print("Correr")
    print("Encender Luces")

objeto_cohe=Coche()
objeto_coche.metodosCoche()

objeto_deportivo=Deportivo()
objeto_deportivo.metodosDeportivo()
objeto_deportivo=Coche()
objeto_deportivo.metodosCoche()