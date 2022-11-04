cadena1="Estoy aprendiendo Python"

#Encontrar contenido
print(cadena1.find("Python"))
print(cadena1.find("Estoy"))

#Cambiar: lower(), upper(), title()
print(cadena1.lower())
print(cadena1.upper())
print(cadena1.title())

#Reemplazar contenido: replace()
print(cadena1.replace("aprendiendo", "desarrollando"))

#Cortar
print(cadena1[0:5])

#Encontrar pt.2: find()
print(cadena1[:10].find("Python")) #(no lo encuentra en la búsqueda#
