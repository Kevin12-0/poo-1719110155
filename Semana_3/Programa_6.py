class Futbolista:
  def __init__(self):
    print("Nombre")
    print("Apellidos")
    print("Equipo")
    print("Posiscion")
    print("Velocidad")
  def metodosFutbolista(self):
    print("Jugar")
    print("Entrenar")
'Subclase 1'
class Basketbolista(Futbolista):
  def __init__(self):
    print("Altura")
    print("Habilidad")
    print("Numero")
    print("Cambio")
    print("Reserva")
  def metodosBasketbolista(self):
    print("Saltar")
    print("Cobrar")

objeto_futbolista=Futbolista()
objeto_futbolista.metodosFutbolista()

objeto_basketbolista=Basketbolista()
objeto_basketbolista.metodosBasketbolista()
objeto_basketbolista=Futbolista()
objeto_basketbolista.metodosFutbolista()