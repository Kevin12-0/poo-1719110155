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
  def pagar(self):
    print("Pago en Ventanilla")
  def consultar(self):
    print("Consultar saldo desde cajero automatico")

objeto_banco=Banco()
objeto_banco.consultar()
objeto_banco.pagar()

Banco_hipotecario=BancoComercial()
Banco_hipotecario.pagar()
Banco_hipotecario.consultar()