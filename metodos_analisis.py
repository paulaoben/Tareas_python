"""
cadena1= "Curso de aprendizaje de Python"

print(cadena1.count("de"))
print(cadena1.find("de"))
print(cadena1.rfind("de"))

#Booleanos#
print(cadena1.startswith("Curso"))
print(cadena1.endswith("Curso"))
print(cadena1.endswith("Python"))

"""

#str.isnumeric

numero = "125"
print(numero.isnumeric())

palabra = "Paula"
print(palabra.isnumeric())

alfanum = "p00"
print(alfanum.isnumeric())

"""Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric."""

#str.isdigit

print(numero.isdigit())
print(palabra.isdigit())
print(alfanum.isdigit())

"""Return true if all characters in the string are digits and there is at least one character, false otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal."""

#Otros ejemplos

#Para letras
abc = "qwerty"
print(abc.isalpha())

#Para alfanuméricos
alf = "20te"
print(alf.isalnum())

