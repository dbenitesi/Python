# 🚨 Don't change the code below 👇
altura = float(input("enter your height in m: "))
peso = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(peso / (altura*altura))
resultado = round(BMI)

if BMI <= 18.5:
    print(f"Your BMI is {resultado}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {resultado}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {resultado}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {resultado}, you are obese.")
else:
    print(f"Your BMI is {resultado}, you are clinically obese.")

        