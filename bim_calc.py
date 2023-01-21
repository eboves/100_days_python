input_name = input("What is your name? ").title()
persons_weight = float(input(f"Hi {input_name} can you please enter you WEIGHT in LBS. "))
persons_height = float(input(f"Hi {input_name} can you please enter you HEIGHT in FT ")) * 12

bmi = round((persons_weight/persons_height**2)* 703, 2)
print(f"{input_name}, your BMI is: {bmi}")