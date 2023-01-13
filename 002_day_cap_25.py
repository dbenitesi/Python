# Challenge
# Crear un programa que calcule cuantos dias, semanas y meses quedan 
# si vivieramos hasta los 90 anos.

# El programa solo preguntara por la edad del usuario

print("***************************************************************************************")
print("############ PROGRAMA QUE CALCULA LO QUE TE QUEDA POR VIVIR ###########################")
print("#######################################################################################\n")
anos = int(input("                            Ingrese su edad: "))
#print(type(anos))
dias = anos * 365
semanas = anos * 52
meses = anos * 12
dias_v = 32850 - dias
semanas_v = 4692 - semanas
meses_v = 1080 - meses

print(f"             Has vivido: {dias} dias, {semanas} semanas, {meses}meses")
print(f"             Te queda por vivir {dias_v} dias, {semanas_v} semanas, {meses_v} meses")


