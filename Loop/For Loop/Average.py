# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalheight = 0
for height in student_heights:
    totalheight += height

student = 0
for students in student_heights:
    student += 1

average = round(totalheight / student)
print(f"The average height is {average}")
    



