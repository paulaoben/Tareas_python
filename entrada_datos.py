#Solicitar información al usuario a través del teclado la información que ingresa será de tipo cadena

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad ")

""" int() modifica el tipo de dato para que deje de ser str, sin embargo no va a aceptar decimales por lo que convendría utilizar float
sueldo = int(input("Ingrese su sueldo ")) +500"""
sueldo = float(input("Ingrese su sueldo ")) +500

print("Su nombre es:", nombre)
print("Su edad es:", edad)
print("Su sueldo es:", sueldo)
