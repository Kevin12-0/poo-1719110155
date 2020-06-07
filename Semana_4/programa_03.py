class Avion:
  def __init__(self):
    print("Marca")
    print("modelo")
    print("Tipo de combustible")
    print("Pilotos")
  def metodosAvion(self):
    print("volar")
    print("trasportar")
class Avioneta(Avion):
  def __init__(self):
    print("Alerones")
    print("Motores")
    print("Llantas")
    print("Asientos")
    print("Aerolinea")
  def metodosAvioneta(self):
    print("planear")
    print("acuatisar")
  def metodosAvion(self):
    print("Volar a una menor escala")
    print("Trasportar carga o pocas personas")
objeto_avion=Avion()
objeto_avion.metodosAvion()

objeto_avioneta=Avioneta()
objeto_avioneta.metodosAvion()
objeto_avioneta.metodosAvioneta()