person_name = input("Please enter your name: ").title()
print(f"Hi {person_name}, Welcome to the tip calculator.")
total_bill = float(input("What was the total bill: $ "))
percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15% ")) / 100
amount_split = int(input("How many people are you splitting the bill? "))

amount_to_pay = round((total_bill + (total_bill * percentage)) / amount_split, 2)
print(f"Each person should pay: ${amount_to_pay}")