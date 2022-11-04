# mi_diccionaario = {"key1":<value1>, "key2":<value2>, "key3":<value3>}

#Declaraar el diccionario
persona = {"Nombre":"Paula", "Apellido":"Ontivero Obenloch", "Edad":250, "Tecnología":"Python"}
print(persona)
print(persona["Edad"])

#Modificar un elemento
persona["Edad"]=25
print(persona)

#Eliminar elemento del diccionario
del persona["Tecnología"]
print(persona)

#Da la respuesta (El valor de la clave)
print(persona.get("Apellido"))

#Si no existe (porque no está o fue mal escrito) ---> None
print(persona.get("Apellidos"))

#Para saber las claves que tiene el diccionario
print(persona.keys())

#Para saber los valores que existen
print(persona.values())