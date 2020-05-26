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
'Subclase 2'
class BancoHipotecario(Banco):
  def __init__(self):
    print("BANCO HIPOTECARIO")
    print("Inverciones")
    print("reformas")
    print("Cuetas")
    print("compañia")
    print("dueño")
  def metodosBancoHipotecario(self):
    print("Grantias")
    print("cedulas")
objeto=Banco()
objeto.pagar()
objeto.consultar()

objeto_banco_comercial=BancoComercial()
objeto_banco_comercial.metodosBancoComercial()
objeto_banco_comercial.pagar()
objeto_banco_comercial.consultar()

objeto_banco_hipotecario=BancoHipotecario()
objeto_banco_hipotecario.metodosBancoHipotecario()
objeto_banco_hipotecario.pagar()
objeto_banco_hipotecario.consultar()