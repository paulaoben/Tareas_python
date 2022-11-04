#Escenario de mutación --> listaas != tuplas

myself = ["Paula", "Ontiver0", "Obenloch", 1997]

print(myself)

myself[1]="Ontivero"

print(myself)

#Impresión del último contenido
print(myself[-1])

#Impresión contenido específico
print(myself[1:3])

#Agregaar UN elemente en la última parte de la lista
myself.append("desarrolladora y estudiante de diseño")
print(myself)

#Agregar MÁS DE UN elemento en la última parte de la lista
myself.extend(["Manejo de diferentes tecnologías como", "HTML, CSS, JAVASCRIPT, PYTHON y GIT"])

"""Efecto: .append() agrega un elemento al final de la lista mientras que .extend() puede agregar varios elementos de una secuencia al final de la lista.
Argumento: .append() toma un solo elemento como argumento mientras que .extend() toma un iterable como argumento (por ejemplo: listas, tuplas, diccionarios, sets, y cadenas de caracteres)."""

#Agregar contenido en una parte específica de la lista
myself.insert(1, "Valeria")
print(myself)

#Busca la posición de un elemento en la lista
print(myself.index(1997))

#Eliminar un elemento de la lista
print(myself.remove("Valeria"))
print(myself)

#Verificar existencia del contenido
#agregar uno para demostrar el efecto
myself.append(1997)
print(myself)
print(myself.count(1997))

yourself = ["María", "Victoria", "Gómez",  2002]
print(yourself)

us = myself + yourself

print(us)