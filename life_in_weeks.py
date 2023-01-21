from turtle import title


person_name = input("Can you please enter your name: ").title()
person_age = float(input(f"Hi {person_name}, can you please enter your age: "))
years_til_90 = 90 - person_age
days_til_90 = int(years_til_90 * 365)
weeks_til_90 = int(years_til_90 * 52)
months_til_90 = int(years_til_90 * 12)

print(f"Hi {person_name}, you have {days_til_90} days, {weeks_til_90} weeks, and {months_til_90} months left.")