userInput = input("Enter a 2 digits number ")
first_digit = int(userInput[0])
second_digit = int(userInput[1])
suma = str(first_digit + second_digit)
if len(suma) > 1:
    fist_digit_suma = int(suma[0])
    second_digit_suma = int(suma[1])
    final_suma = str(fist_digit_suma + second_digit_suma)
    print("The suma = " + suma)
    print("The final suma = " + final_suma)
else:
    print("The sum = " + suma)

