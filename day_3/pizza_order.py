print("Welcome to Python Pizza Deliveries!")
print("""
Here are the Prices:
Small Pizza = $15
Medium Pizza = $20
Large Pizza = $25

Toppins:
Pepperoni for Small Pizza = +$2
Pepperoni for Medium or Large Pizza = +$3

Extra cheese for any size pizza = +$1
""")
person_name = input("Please enter your name: ").title()
size = input(f"{person_name}, What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input(f"{person_name}, do you want pepperoni? Y or N: ").upper()
extra_cheese = input(f"{person_name}, do you want extra cheese? Y or N: ").upper()
bill = 0

if size == 'S':
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"{person_name}, Your order was: {size} Pizza, you said {add_pepperoni} Pepperoni and you said {extra_cheese} Extra-Cheese")
print(f"{person_name}, Your final bill is: ${bill}")