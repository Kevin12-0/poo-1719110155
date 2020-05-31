'Clase maestra'
class Banco:
  def __init__(self):
    print("Cajeros")
    print("ventanilla")
    print("compañia")
    print("dueño")
    print("atencion a clientes")
  def pagar(self):
    print("Pagar")
  def consultar(self):
    print("consultar")
'Subclase 1'
class BancoComercial(Banco):
  def __init__(self):
    print("BANCO COMERCIAL")
    print("divisa")
    print("creditos")
    print("fondos publicos")
    print("compañia")
    print("dueño")
  def metodosBancoComercial(self):
    print("Gestionar")
    print("Administrar")

objeto_banco=Banco()
objeto_banco.pagar()
objeto_banco.consultar()

objeto_banco_comercial=BancoComercial()
objeto_banco_comercial.metodosBancoComercial()
objeto_banco_comercial.pagar()
objeto_banco_comercial.consultar()
objeto_banco_comercial=Banco()
