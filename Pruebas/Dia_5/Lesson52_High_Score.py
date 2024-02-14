student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
maxi = 0
piso = 1
# for student in student_scores:
#     if student > piso:
#         maxi = student
#         print(maxi)        
#     piso = maxi
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#print("The highest score in the class is: " + str(maxi)) 

#Write your code below this row 👇

