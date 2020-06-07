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
  def metodosFutbolista(self):
    print("Jugar en un esadio de Basketball")
    print("Entrenar en las instalaciones del Equipo")
objeto_futbolista=Futbolista()
objeto_futbolista.metodosFutbolista()

objeto_basketbolista=Basketbolista()
objeto_basketbolista.metodosBasketbolista()
objeto_basketbolista.metodosFutbolista()