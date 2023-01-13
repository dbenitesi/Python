#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_random = 0
symbols_random = 0
numbers_random = 0
everything = []
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#everything = letters + numbers + symbols

for i in range(1, nr_letters + 1):
        letters_random = random.choice(letters)
        everything.append(letters_random)

for i in range(1,nr_symbols + 1):
        symbols_random = random.choice(symbols)
        everything.append(symbols_random)

for i in range(1, nr_numbers + 1):
        numbers_random = random.choice(numbers)
        everything.append(numbers_random)

#password_len = nr_letters + nr_symbols + nr_numbers

# for i in range(password_len):
#         caracter_random = random.choices(everything)
#         password.append(caracter_random)

#password = "".join(password)
#print(f'Tu password segura es: {everything}')
random.shuffle(everything)
#print(everything)
everything = ''.join(everything)
print(everything)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P