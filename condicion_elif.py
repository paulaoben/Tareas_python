#Elif es una segunda condición que aparece de manera posterior al if, en caso de ser falsa, entonces va hacia else

edad = int(input("Ingrese su edad: "))
if edad<18:
    print("Usted es menor de edad")
elif edad==18:
    print("Su edad es de 18 años")
else:
    print("Usted es mayor de edad, por encima de los 18 años")

"""Las condiciones serán evaluadas de manera secuencial por lo tanto IMPORTA EL ORDEN en el que se escriben"""