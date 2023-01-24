# lover_1 = input("Hi, please enter your full-name: ").lower()
# lover_2 = input("Hi, please enter the full-name of you belover: ").lower()

lover_1 = "david beckham"
lover_2 = "victoria beckham"

combine_names = lover_1 + lover_2

t = combine_names.count('t')
r = combine_names.count('r')
u = combine_names.count('u')
e = combine_names.count('e')

true = str(t + r + u + e)

l = combine_names.count('l')
o = combine_names.count('o')
v = combine_names.count('v')
e = combine_names.count('e')

love = str(l + o + v + e)

percentage = int(true + love)

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}")





