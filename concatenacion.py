Nombre= "Paula"
Apellido= "Ontivero Obenloch"
Especialidad= "Desarrolladora"

#Primera forma de concatenación
print(Nombre , " " + Apellido)

#Segunda forma de concatenación
print("Mi nombre es %s " %Nombre)
print("Mi nombre es %s y mi apellido es %s " %(Nombre , Apellido))

#Tercera forma de concatenación
print("Mi nombre es {0} y mi especialidad es {1}".format(Nombre , Especialidad))

#Cuarta forma de concatenación
print("Mi nombre es: {a} y mi apellido es {b}".format(a=Nombre, b=Apellido))
