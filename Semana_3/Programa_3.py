class Avion:
  def __init__(self):
    print("Marca")
    print("modelo")
    print("Tipo de combustible")
    print("Pilotos")
  def metodosAvion(self):
    print("volar")
    print("trasportar")
'subclase 1'
class Avioneta(Avion):
  def __init__(self):
    print("Alerones")
    print("Motores")
    print("Llantas")
    print("Asientos")
    print("Aerolinea")
  def metodosAvioneta(self):
    print("planar")
    print("acuatisar")

objeto_avion=Avion()
objeto_avion.metodosAvion()

objeto_avioneta=Avioneta()
objeto_avioneta.metodosAvioneta()
objeto_avioneta=Avion()
objeto_avioneta.metodosAvion()