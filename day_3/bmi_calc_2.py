person_name = input("Please enter your name: ").title()

persons_weight = float(input(f"Hi {person_name} can you please enter you WEIGHT in LBS. "))
persons_height = float(input(f"Hi {person_name} can you please enter you HEIGHT in FT ")) * 12

bmi = round((persons_weight/persons_height**2)* 703, 2)
if 0 < bmi < 18.5:
    print(f"{person_name}, your BMI is {bmi}, you are UNDERWEIHT.")
elif 18.5 <= bmi < 25:
    print(f"{person_name}, your BMI is {bmi}, you have a NORMAL WEIGHT.")
elif 25 <= bmi < 30:
    print(f"{person_name}, your BMI is {bmi}, you are OVEREIGHT.")
elif 30 <= bmi < 35:
    print(f"{person_name}, your BMI is {bmi}, you are OBESE.")
elif bmi >= 35:
    print(f"{person_name}, your BMI is {bmi}, you are CLINICALLY OBESE.")
else:
    print(f"{person_name}, Please enter a valid number.")
