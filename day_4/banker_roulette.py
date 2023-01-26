import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_picker = random.randint(0, len(names))
print(names[random_picker])