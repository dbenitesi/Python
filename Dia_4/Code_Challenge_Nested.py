# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
print(type(position))
segundo_indice = int(position[0])-1
primer_indice = int(position[1])-1
if primer_indice == 0:
    row1[segundo_indice] = 'X'
    print(f"{row1}\n{row2}\n{row3}")
elif primer_indice == 1:
    row2[segundo_indice]  = 'x'
    print(f"{row1}\n{row2}\n{row3}")
else:
    row3[segundo_indice]  = 'x'
    print(f"{row1}\n{row2}\n{row3}")


#Write your code below this row 👇

