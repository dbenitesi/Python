# Code Challenge from the 5th Day of the program 100 Days of Code.
# https://www.hackerrank.com/domains/tutorials/100-days-of-code - Revisar el link. LLenado por Github Co_Piloto.

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

ramdon_name = len(names)
random_integer = random.randint(0, ramdon_name)
print("El que debe pagar la comida es " + names[random_integer])



#print(ramdon_name, type())



#Write your code below this line 👇
