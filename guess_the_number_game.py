# Import "random" library
import random

# Intro
print("GUESS THE NUMBER GAME! ¨\n")
player_name = input("Insert your name: ")
print(f"Welcome! {player_name}. Please choosse the range of numbers.")
min_number = input("Enter the lowest number:")
max_number = input("Enter the highe}st number: ")


# Game Conditions
if not((min_number.isdigit()) and (max_number.isdigit())):
    print("Some or both value(s) you entered are not digits. PLEASE, TRY AGAIN!")
else:
    print(f"MINIMUM number is: {min_number} | MAXIMUM number is: {max_number}.")

# Generate target number
min_number = int(min_number)
max_number = int(max_number)
target_number = random.randrange(min_number, max_number)

# Main
attempts = 5
player_guess = None
while (attempts > 0):       
    attempts -= 1
        
    # Get player's guess
    while True:
        try:
            player_guess = int(input(f"Pick a NUMBER between {min_number} and {max_number}: "))
            break  # Exit loop if the input is a valid number
        except ValueError:
            print("The input is not a valid number. Please input a number.")
    
    # Game logic
    if player_guess == target_number:
        print(f"CONGRATS, YOU WON THE GAME in {5 - attempts} attempts!")
        print(f"The winning number is {target_number}.")
        break
    elif player_guess < target_number:
        print(f"{player_name}´s choice: {player_guess}")
        print(f"You picked a LOWER number.")
        if(attempts != 0):
            print(f"{attempts} attempts left.")
        else:     
            print(f"GAME OVER :( ! THE WINNING NUMBER WAS: {target_number})")
        
    else:
        print(f"{player_name}´s choice: {player_guess}")
        print(f"You picked a HIGHER number. Try again!")
        if(attempts != 0):
            print(f"{attempts} attempts left.")
        else:
            print(f"GAME OVER :( ! THE WINNING NUMBER WAS: {target_number})")
    
    
print(f"HEY! {player_name}! THANK YOU FOR PLAYING!")
