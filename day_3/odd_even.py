person_name = input("Please enter your name: ").title()
number_entered = int(input(f"Hi {person_name}, Enter an interger please: "))

odd_even = f"{person_name}, you entered the Even number {number_entered}." if number_entered % 2 == 0 else f"{person_name}, you entered the Odd number {number_entered}"
print(odd_even)