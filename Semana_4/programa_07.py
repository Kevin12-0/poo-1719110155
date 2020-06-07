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
  def metodosCoche(self):
    print("Acelerar pisando el acelerador ")
    print("Frenar pisando el pedal de ")
objeto_coche=Coche()
objeto_coche.metodosCoche()

objeto_deportivo=Deportivo()
objeto_deportivo.metodosDeportivo()
objeto_deportivo.metodosCoche()