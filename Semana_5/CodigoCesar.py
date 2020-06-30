class CodigoCesar: #Definimos la clase
    def  __init__(self): #Definimos el metodo constructor
        pass 
    def cifradoDesifrado(self): #metodo que cifrara y descifrara
        respuesta="S" #variable que ayudara al ciclo while
        cifrado="" #variable ayudara a guardar el texto cifrado
        desifrado="" #variable que ayudara a guardar el texto
        while respuesta=="S" or respuesta=="s": #Si respuesta es S o s
            cadena=input("Inserta tu cadena ") #Insertar tu cadena desde el teclado
            preguta=input("Desea cifrar o desifrar? ") #Pregunta la accion que quieres hacer con la cadena
            if preguta=="Cifrar" or preguta=="cifrar": #si es cifrar
                for scannear in cadena: #lee la variable cadena
                    alfabeto=ord(scannear) #convierte tu cadena en codigo ASCII
                    cifrado+=chr(alfabeto-(7*2)) #convierte tu codigo ASCCI en caracter pero restandole 14
                print(cifrado)#te imprime tu cadena ya cifrada
            elif preguta=="Desifrar" or preguta=="desifrar": #si es desifrar
                for scannear in cadena: #Lee la variable cadena
                    alfabeto=ord(scannear)#la variable scannear del ciclo for la convierte en ASCCI
                    desifrado+=chr(alfabeto+(7*2))#Convierte tu codigo ASCCI a caracter teniendo sumandole 14
                print(desifrado) #imprime tu texto ya desifrado
            respuesta=input("Desea cifrar o desifrar otra cadena ?") #pregunta si deseas cifrar o desifrar otra cadena
            if respuesta=="N" or respuesta=="n": #si la respuesta es N o n
                break #se termina el codigo
objeto_cifrado=CodigoCesar() #llamamos a la clase
objeto_cifrado.cifradoDesifrado() #llamamos al metodo que ara todas la funciones.