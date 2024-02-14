# CLASE DE IF / ELSE
# Crear un programa condicional para vender tickets
# dependiendo de la altura

# El programa pregunta la altura, y segun el condicional vende el ticket

print("***************************************************************************************")
print("############ PROGRAMA QUE VENDE TICKETS SEFUN LA ALTURA DE LA P ########################")
print("#######################################################################################\n")
print("                     BIENVENIDOS A LA MONTANA RUSA DE LA DIVERSION                      \n")
altura= int(input("Ingrese su altura en cm: "))
if altura >= 120:
    print("\nTicket Vendido\n")  
else:
    print("\nNo cumple con los parametros para comprar ticket\n")
