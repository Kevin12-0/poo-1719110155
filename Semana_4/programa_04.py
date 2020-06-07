class Vacaciones:
  def __init__(self):
    print("Lugar")
    print("Fecha de salida")
    print("Costo")
    print("Personas")
    print("Alojamiento")
  def metodosVacaciones(self):
    print("Descansar")
    print("Disfrutar")
class Retiro(Vacaciones):
  def __init__(self):
    print("Hora de salida")
    print("Hora de regreso")
    print("Personas")
    print("Actividades")
    print("Ahorros")
  def metodosRetiro(self):
    print("Entretener")
    print("Pensar")
  def metodosVacaciones(self):
    print("Descansar en algun lugar retirado")
    print("Disfrutar la soledad")

objeto_vacaciones=Vacaciones()
objeto_vacaciones.metodosVacaciones()

objeto_retiro=Retiro()
objeto_retiro.metodosRetiro()
objeto_retiro.metodosVacaciones()
