# Realizar un algoritmo que pinte la letra U por pantalla hecha con asteriscos.
# El programa pedirá la altura. 
# Fíjate que el programa inserta un espacio y pinta dos asteriscos menos en la base
# para simular la curvatura de la letra.
# Es importante indicar al usuario que la altura mínima debe ser de 4.
# 
# Ejemplo 1:
# Introduzca la altura de la U: 5
# 
# *     *
# *     *
# *     *
# *     *
#   *** 
# print(espacio + "*" + espacio + "*" * tamano2 )

tamano = int(input("Introduce un número  entero para la altura de la U: "))
espacio = " "
if tamano <=3: 
    print("El tamaño de la altura ha de ser mayor de 4")
elif  tamano > 3: 
    for i in range(tamano):
        tamano2 = tamano -1
        print(espacio + "*" + espacio + "*" * tamano2 )
    tamano2 = tamano -1
    
        
        

    




tamano = int(input("Introduce el número entero para la altura de U: "))










# Ejemplo 2:

# Introduzca la altura de la U: 4

# *    *
# *    *
# *    *
#   **