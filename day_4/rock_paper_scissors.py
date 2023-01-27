import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
lista = [rock, paper, scissors]


player_name = input("Please enter your name: ").title()
player = int(input(f"Hi {player_name}, choose between: 0 for Rock, 1 for Paper, 2 for Scissors: "))
# player = int(input("Choose between: 0 for Rock, 1 for Paper, 2 for Scissors: "))

player_chose = lista[player]
print(f"{player_name}, you chose: ")
# print("You chose: ")
print(player_chose)

comp = random.randint(0, len(lista) - 1)
print("Computer chose: ")
print(lista[comp])

if player == comp:
    print("DRAW")
elif player == 0 and comp == 2:
    print("You Won")
elif player == 1 and comp == 0:
    print("You Won")
elif player == 2 and comp == 1:
    print("You Won")
else:
    print("You Lose")