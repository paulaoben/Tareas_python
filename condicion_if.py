#Esta instrucción nos permite condicionar la ejecución de uno o varios bloques dentro de nuestra codificación siempre y cuando se cumpla, el proceso se aplicará y también tiene partes contrarias en el caso de que no se cumpla

"""if condición
    acá irían las órdenes que se ejecutarán si la condición es cierta y que pueden ocupar varias líneas (siempre hay que tabularlas)"""

edad = int(input("Ingrese su edad: "))

if edad>=18:
    print("Usted es mayor de edad")

#Hasta acá si no se cumple la condición posteriormente no sucedería nada más ya que no se le indicó, sino que se finaliza el proceso.

else:
    print("Usted es menor de edad")

#Else indica qué sucederá si no se cumple la condición de if

