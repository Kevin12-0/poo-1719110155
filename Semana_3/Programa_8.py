class Calculadora:
  def __init__(self):
    print("Altura")
    print("Color")
    print("Peso")
    print("Marca")
    print("Modelo")
  def metodosCalculadora(self):
    print("Sumar")
    print("Multiplicar")
'Subclase 1'
class CalculadoraCientifica(Calculadora):
  def __init__(self):
    print("Teaclas")
    print("Memoria")
    print("Funciones")
    print("Alimentacion")
    print("Pantalla")
  def metodosCalculadoraCientifica(self):
    print("Divir")
    print("Funciones Trigonometricas")

objeto_calculadora=Calculadora()
objeto_calculadora.metodosCalculadora()

objeto_cientifica=CalculadoraCientifica()
objeto_cientifica.metodosCalculadoraCientifica()
objeto_cientifica=Calculadora()
objeto_cientifica.metodosCalculadora()