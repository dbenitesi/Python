# # num_char = len(input("Whats is your name?"))
# # new_num_char = str(num_char)
# #print("Your name has " + new_num_char + " characters")
# #print(type(num_char))

# cadena = input("Esto que escribiras es una cadena: ")

# print(type(cadena))
# #uno_cadena = int(cadena[0])
# #dos_cadena = int(cadena[1])
# #resultado = uno_cadena + dos_cadena
# suma = int(cadena[0])+int(cadena[1])
# print(suma)

# 39
# print(3*(3+3)/3-3)

from tokenize import Double
from unittest import result


altura = float(input("Introduzca su altura: "))
peso = float(input("Introduzca su peso: "))

BMI = float(peso / (altura*altura))
resultado = "Su BMI es %2.2f" %(BMI)
print(resultado)