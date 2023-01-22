# Leap year evenly divisible by 4 
# unless is exactly divisible by 100 
# unles is also divisible by 400

person_name = input("Please enter your name: ").title()

year_entered = int(input(f"{person_name}, please enter a year. "))

if year_entered % 4 == 0:
    if year_entered % 100 == 0:
        if year_entered % 400 == 0:
            print(f"{person_name}, you entered a Leap Year, {year_entered}")

        else:
            print(f"{person_name}, you entered a Regular Year, {year_entered}")

    else:
        print(f"{person_name}, you entered a Leap Year, {year_entered}")

else:
    print(f"{person_name}, you entered a Regular Year, {year_entered}")
