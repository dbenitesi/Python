# Lesson 51 - For Loops 
# Using the For Loop with Python Lists
#fruits = ['Apple', 'Peach', 'Pearl']

# This for runs through List ands prints its value, Givin the value to the variable fruit
# for fruit in fruits:
#     #print(fruit)
#     print(fruit + " Pie")  

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    #print(student_heights)      
# 🚨 Don't change the code above 👆18
final = 0
i = 0
for count in student_heights:
    final = final + count
    i = i + 1
approx = final / i
print(round(approx))    

#Write your code below this row 👇


