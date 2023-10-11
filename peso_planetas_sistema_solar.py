def calcular_peso_en_planeta(peso_tierra, gravedad_planeta): 
#Se define la función con la que se guardará el peso de la tierra para posteriormente ser multiplicado por la gravedad del planeta. 
    peso_planeta = peso_tierra * gravedad_planeta
    return peso_planeta

def main(): #Main es el método principal del programa, el def ejecuta todo lo que hay dentro del main.
    gravedad_planetas = {
      "Mercurio" : 3.7,
      "Venus" : 8.87,
      "Tierra" : 9.81,
      "Marte" : 3.71,
      "Jupiter" : 24.79,
      "Saturno" : 10.44,
      "Urano" : 8.69,
      "Neptuno" : 11.15,
    } #Diccionario donde se guardan los valores de las gravedades que serán usadas en las operaciones.
    try: #Try hace que se intente hacer todo lo que este dentro a no ser que haya un error que luego se ejecutará en el except.
        peso_en_tierra = float(input("Tu peso en la Tierra(en kg): "))

        while True:
            print("Elige un planeta del sistema solar: ")
            for i, planeta in enumerate(gravedad_planetas.keys(), 1): #i almacena el número de lineas que tiene el diccionario.
            #enumarate que la lista empiece desde el número 1 en vez desde el cero.
            #.keys coge las "keys" del diccioario que en este caso es el nombre de los planetas.
                print(f"{i}. {planeta}") #La f da formato y permite imprimir el valor de variables.
            print("0. Salir del programa")
            opcion = int(input("Elige el número del planeta o si quieres salir, pulsa 0:")) #opcion analiza la respuesta del input para llevarlo al número previamente explicado.

            if opcion == 0:
                break #Cuando el número introducido es 0 se rompe el bucle.
            elif opcion < 1 or opcion > len(gravedad_planetas): #elif ejecuta cuando courre lo contrario de if.
            #Len marca el límite del diccionario.
                print("Opción no valida. Pon un número válido.")
            else:
                planetas = list(gravedad_planetas.keys()) #lista del diccionario previamente explicado y con el.keys con la misma razon que antes.
                planeta_elegido = planetas[opcion - 1] #se pone la opcion -1 porque previamente en el codigo con el enumerate se puso que se empezarían a enumerar los planetas con el número 1.
                gravedad_elegida = gravedad_planetas[planeta_elegido] 

                peso_en_planeta = calcular_peso_en_planeta(peso_en_tierra, gravedad_elegida)
                print(f"Tu peso en {planeta_elegido} es igual a {peso_en_planeta: .2f} kilogramos. ") #2f funciona para que el número pueda ser decimal, basicamente como un float.
    except ValueError: #Except hace que no se ejecute el bucle si hay un ValueError
        print("Pon un número válido como peso en la Tierra.")
main()#Cerrar el main


            



