# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(t)
name1_lower = name1.lower()
name2_lower = name2.lower()
t = name1_lower.count("t")+name2_lower.count("t")
r = name1_lower.count("r")+name2_lower.count("r")
u = name1_lower.count("u")+name2_lower.count("u")
e1 = name1_lower.count("e")+name2_lower.count("e")
l = name1_lower.count("l")+name2_lower.count("l")
o = name1_lower.count("o")+name2_lower.count("o")
v = name1_lower.count("v")+name2_lower.count("v")
e = name1_lower.count("e")+name2_lower.count("e")
r_1 = t+r+u+e1
r_2 = l+o+v+e
r_3_m = str(r_1)+str(r_2)
r_3 = int(r_3_m)
if r_3 < 10 or r_3 > 90:
    print(f"Your score is {r_3}, you go together like coke and mentos.")
elif r_3 <50 and r_3 >40:
    print(f"Your score is {r_3}, you are alright together.")
else:
    print(f"Your score is {r_3}.")

