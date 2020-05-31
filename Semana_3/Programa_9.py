class CajeroAutomatico:
  def __init__(self):
    print("Compañia")
    print("Color")
    print("Funciones")
    print("Pantalla")
    print("Teclado")
  def metodosCajeroAutomatico(self):
    print("Depositar")
    print("Retirar")
'Subclase 1'
class CajeroFull(CajeroAutomatico):
  def __init__(self):
    print("Tamaño")
    print("Scanner")
    print("Fuente de eneregia")
    print("Reconocimiento")
    print("Modelo")
  def metodosCajeroFull(self):
    print("Transferir")
    print("Pagar")

objeto_cajero=CajeroAutomatico()
objeto_cajero.metodosCajeroAutomatico()

objeto_cajero_full=CajeroFull()
objeto_cajero_full.metodosCajeroFull()
objeto_cajero_full=CajeroAutomatico()
objeto_cajero_full.metodosCajeroAutomatico()