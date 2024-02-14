# Challenge
# Crear un programa condicional para vender tickets
# dependiendo de la altura

# El programa pregunta la altura, y segun el condicional vende el ticket

print("***************************************************************************************")
print("############ PROGRAMA QUE VENDE TICKETS SEFUN LA ALTURA DE LA P ########################")
print("#######################################################################################\n")
print("                     NUMERO EVEN Y ODD NUMBER                                         \n")

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

resultado = number % 2
if resultado == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

