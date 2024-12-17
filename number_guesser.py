import random

print("Numbers only please")

number = random.randint(0,100)

lives = 5

while lives != 0:
    try:
        players_guess = int(input("enter a number between 0 and 100: "))
        if players_guess == number:
            print("YOU WIN!! 🎉")
            break
        elif players_guess > number:
            lives -= 1
            print("Your guess was higher than the number")
            print(f"You have {lives} remaining")
            
        elif players_guess < number:
            lives -= 1
            print("Your guess was less than the number")
            print(f"You have {lives} remaining")
    except ValueError:
        print("Numbers only brother!")
if lives == 0:
    print(f"You lost! the number was {number}")
    print("Thanks for playing!")
else:
    print("Thanks for playing!")