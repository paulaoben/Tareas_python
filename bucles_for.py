"""Sintaxis en Python != a JAVA y C#:
for variable in elemento iterable (lista, cadena, range, etc.):
cuerpo del bucle"""

lista=(100, 10, 200)
for x in lista:
    print(x)

for x in range(10):
    print(x)

for x in range(6):
    print(x, end="; ")

numero=5
for x in range(13):
    print(numero, " + ", x , "=", numero+x)

numero=5
for x in range(13):
    print(numero, " * ", x , "=", numero*x)
