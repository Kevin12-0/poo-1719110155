class GoogleClassroom:
  def __init__(self):
    print("Clases")
    print("Alumnos")
    print("profesores")
    print("Calendarios")
    print("Tareas")
  def metodosGoogleClassroom(self):
    print("Entregar")
    print("Comentar")
class SalonDeClases(GoogleClassroom):
  def __init__(self):
    print("Tareas")
    print("Horarios")
    print("Actividades")
    print("Organizacion")
    print("Archiveros")
  def metodosSalonDeClases(self):
    print("Participar")
    print("Entrar")

objeto_google=GoogleClassroom()
objeto_google.metodosGoogleClassrooom()

objeto_salon=SalonDeClases()
objeto_salon.metodosSalonDeClases()
objeto_salon=GoogleClassroom()
objeto_salon.metodosGoogleClassroom()
