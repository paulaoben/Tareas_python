"""Los operadores ternarios son de alguna manera expresiones condicionales que nos permiten evaluar una expresión y dependiendo de si el resultado que se obtiene es verdadero se ejecuta o se aplica un contenido para el caso verdadero y si es falso se aplica un contenido para su caso también"""

nombre = "Paula"

resultado = "Si es Paula" if nombre=="Paula" else "No es Paula"
print(resultado)

nac = "Argentina"

resultado2=("Su nacionalidad no es argentina", "Su nacionalidad es argentina")[nac == "Argentina"]
print(resultado2)


resultado3 = (5<6) or (3>10)
print(resultado3)
