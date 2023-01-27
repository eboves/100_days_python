# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
holder = 0
iterration = 0
for height in student_heights:
    holder += height
    iterration += 1
    print(f"{holder} is: , and height is: {height}")
average = round(holder/iterration)
print(f"The average height is: {average}")