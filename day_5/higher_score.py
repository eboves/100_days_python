# 🚨 Don't change the code below 👇
from textwrap import indent


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

holder = 0
current = student_scores[0]

for score in student_scores:
   if score > current:
       holder = score
       current = score

print(holder)