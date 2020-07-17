respuesta="S" #variable para ayudar al ciclo while
datos = [] #arreglo para ayudar a almacenar los datos
class Alumnos: #creamos una clase
    def __init__(self): #metodo constrcutor
        pass
    def datos(self): #creamos un metodo para perdir datos
        nombre=input("Inseta el nombre del alumno: ") #Pide el nombre del alumno
        año=int(input("Año de nacimeinto del alumno: ")) #pide el año de nacimiento del alumno tipo entero
        grupo=input("Inserta el grupo del alumno: ") #pide el grupo del alumno
        años_total=2020-año #calcula la edad restando el año actual con el año de nacimiento
        datos.append("Nombre:"+str(nombre)+" Edad:"+str(años_total)+" Grupo:"+str(grupo)) #agrega los datos
        #al arreglo datos
    def imprimir(self): #creamos metodo para imprimir los datos capturados
        for leer in datos: #leera el arreglo datos
            print(leer) #imprimira en pantalla los datos capturados por indice
while respuesta=="s" or respuesta=="S": #mientras que la repuesta sea S
    objecto_Almuno=Alumnos() #creamos el objeto
    objecto_Almuno.datos()#se estara llamando al metodo para la captura de datos
    respuesta=input("¿Desea leer mas datos de alumnos? S/N ") #pregunta si deseas hacer mas capturas de alumnos
    if respuesta=="N" or respuesta=="n": #si la respuesta es "N" o "n"
        objecto_Almuno.imprimir() #llama al metodo que permitira imprimir
        break #termina el ciclo del programa