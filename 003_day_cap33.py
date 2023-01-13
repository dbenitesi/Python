# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

primerCheck = year / 4
segundoCheck = year / 100
tercerCheck= year /400

if primerCheck % 1 == 0:
    if segundoCheck % 1 > 0:
        print("Leap year")
    elif tercerCheck % 1 == 0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
