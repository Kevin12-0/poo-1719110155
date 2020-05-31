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
'Subclase 1'
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

objeto_estudiante=Estudiante()
objeto_estudiante.metodosEstudinte()

objeto_recursador=Recursador()
objeto_recursador.metodosRecursador()
objeto_recursador=Estudiante()
objeto_recursador.metodosEstudinte()

