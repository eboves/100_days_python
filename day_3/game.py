player_name = input("Please enter your name: ").title()

left_right_1 = input(f"""Hi {player_name},
                            Welcome to the jumgle, here your skills will be pushed to the limit.
                            You have to get to the next trive the 'PACACHES'. The Pacaches are a civilized city 
                            that is becoming more populated. However you are have to cross the JUNGLE, here you 
                            will find dangerous creatures. 
                            
                            Now choose, 'left' and 'right'""")

if left_right_1 == 'left':
    left_right_2 = input(f"{player_name}, now would you like to swim or walk?, type 'swim' or 'walk'")
    if left_right_2 == 'swim':
        print("GAME OVER.")
    if left_right_2 == 'walk':
        left_right_3 = input(f"{player_name}, now you have to choose from the 3 path in front of you, 'right' 'straight' 'left'")
        if left_right_3 == "right":
            print("GAME OVER.")
        elif left_right_3 == "left":
            print("GAME OVER.")
        else:
            print("You Win!")
else: 
    print("GAME OVER.")
