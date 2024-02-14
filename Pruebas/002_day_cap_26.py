# Challenge
# Crear un programa que calcule el porcentaje de la propina
# entre un numero N de personas

# El programa pregunta la cuenta, el porcentaje y el N de personas

print("***************************************************************************************")
print("############ PROGRAMA QUE CALCULA LA PROPINA Y LA DIVIDE POR N ########################")
print("#######################################################################################\n")

cta = float(input("Introduzca el valor de la cuenta:  "))
porcentaje = int(input("Introduzca que porcentaje dara: 10, 12, o 15?"))
personas = int(input("Introduzca el numero de personas: "))
convPorcentaje = porcentaje * 0.01

pagoPersona = ((cta * convPorcentaje) + cta) / personas
mensaje = "Cada persona debe pagar $%2.2f"%(pagoPersona)
print(mensaje)