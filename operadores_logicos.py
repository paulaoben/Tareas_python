"""Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son <and>, <or> y <not>"""

# Operador---> and ---> devuelve True si ambos operandos son True (uso a and b)

edad=int(input("Ingrese su edad: "))
if edad>=0 and edad<=10:
    print("Usted es un niño")
elif edad>=11 and edad<=17:
    print("Usted es un joven")
else:
    print("Usted es un adulto")

print("Final del proceso")

# Operador---> or ---> devuelve True si alguno de los operandos es True (uso a or b)

edad=int(input("Ingrese su edad: "))
if edad==10 or edad==12:
    print("Su edad se encuentra entre los 10 y los 12 años")
else:
    print("No hay definición para su edad")

print("Final del proceso")

# Operador---> not ---> devuelve True si alguno de los operandos son False (uso not a). Cuando es el operador not hay que tener cuidado porque si es verdadero, va a ser falso y visceversa


edad=int(input("Ingrese su edad: "))
if not edad==10:
    print("Su edad es 10 años")
else:
    print("No hay información sobre su edad")