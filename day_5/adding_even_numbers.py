acumulator = 0
for number in range(1, 101):
    if number % 2 == 0:
        acumulator += number
print(acumulator)