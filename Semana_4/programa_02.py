class Estudiante:
  def __init__(self):
    print("Nombre")
    print("Apellidos")
    print("Edad")
    print("Matricula")
    print("Asignatiura")
  def metodosEstudinte(self):
    print("Aprender")
    print("Leer")
class Recursador(Estudiante):
  def __init__(self):
    print("Grado")
    print("Promedio")
    print("Altura")
    print("Nacionalidad")
    print("Escuela")
  def metodosRecursador(self):
    print("Esudiar")
    print("Escribir")
  def metodosEstudinte(self):
    print("Aprender obligatoriamente")
    print("Leer mas fluido")

objeto_estudiante=Estudiante()
objeto_estudiante.metodosEstudinte()

objeto_recursador=Recursador()
objeto_recursador.metodosRecursador()
objeto_recursador.metodosEstudinte()