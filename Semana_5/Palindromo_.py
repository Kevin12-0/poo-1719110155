class Palindromo:  # declaracion de la clasee maestra
    def __init__(self):  # metodo constructor
        pass

    def cadena(self):  # metodo que ara las comparaciones de las cadenas
        respuesta = "S"  # variable respuesta
        while respuesta == "S" or respuesta == "s":  # si respuepuesta es igual a S o s se cumple y hara el resto del cogigo
            palabra = input("Inserta tu cadena: ")  # lee lo que se esta mandando por el teclado
            contador_espacios = 0 #Almacenara el numero de espacios
            cadena = palabra.lower()  # convierte a minusculas todo
            for espacios in cadena: #scanneara la cadena
                if espacios in " ": #cada que encuentre un espacio lo va a contavilisar
                    contador_espacios+=1 #cada espacio que encuentre lo contavilisa
            print("Tu cadena tiene el siguiente numero de espacios: "+str(contador_espacios))
            palabra = palabra.lower()  # convierte mayusculas a minisculas
            palabra = palabra.replace(" ", "")  # elimina los espacios de una cadena
            palabra=palabra.replace("á","a")
            palabra = palabra.replace("é", "e")
            palabra = palabra.replace("í", "i")
            palabra = palabra.replace("ó", "o")
            palabra = palabra.replace("ú", "u")
            contador_vocales = 0 #almacena el numero de vocales
            for vocales in cadena: # scannea todos los valores de cadena
                if vocales in "aeiouáéíóú": #compara el valor de vocales con las vocales para saber cuantas hay
                    contador_vocales += 1 #cada que haya una vocal se contavilisa
            print("Tu cadena tiene el sieguiente numero de vocales: "+str(contador_vocales))
            inervtida = ""  # variable para almacenar la cadena que se va a invertir
            for i in palabra:  # el valor de i tendra como inicio la ultima letra de la cadena, hasta llegar a
                # el ultimo rango de esta
                inervtida = i + inervtida  # el valor de invertida sera la cadena al reves que se dio gracias al ciclo for
            if palabra == inervtida:  # compara si la cadena es un Palindromo
                print("Palindromo")  # si es Palindromo se imprime el mensaje
            else:  # si no es Palindromo
                print("No es palindromo")  # imprime el siguiente mensaje
            respuesta = input("Desea analizar otra cadena?s/n")  # pregunta si deseas anilizar otra cadena
            if respuesta == "N" or respuesta == "n":  # si la respuesta es N o n
                break  # se deja de ejecutar el codigo
objeto_igualdad = Palindromo()  # se llama a la clase objeto
objeto_igualdad.cadena()  # se hace uso de las funcion qeu contiene el demas resto del codigo