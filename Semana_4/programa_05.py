class Serie_TV:
  def __init__(self):
    print("Actores")
    print("Nombre")
    print("Guion")
    print("Hora de transmicion")
    print("Canal")
  def metodosSerieTV(self):
    print("Entretener")
    print("Distraer")
class Novela(Serie_TV):
  def __init__(self):
    print("Numero de capitulos")
    print("Clasificacion")
    print("Protagonista")
    print("Antagonista")
    print("Extras")
  def metodosNovela(self):
    print("Aburrir")
    print("Interesar")
  def metodosSerieTV(self):
    print("Entrener con la historia")
    print("Distraer por su contenido")

objeto_serie_tv=Serie_TV()
objeto_serie_tv.metodosSerieTV()

objeto_novela=Novela()
objeto_novela.metodosNovela()
objeto_novela.metodosSerieTV()