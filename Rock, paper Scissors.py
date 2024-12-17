import random

print("Welcome to the rock, paper scissors game. The game is best out of 5")
print("------------------------------------------------------")

player_score = 0
computer_score = 0

options = ["Rock", "Paper", "Scissors"]

while player_score < 3 and computer_score < 3:
    player1 = input("Select: Rock, Paper or Scissors: ").lower()
    computer = random.choice(options).lower()

    if player1 not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice.")
        continue
    elif player1 == "paper" and computer == "rock":
        print("YOU WIN!!")
        player_score += 1

    elif player1 == "scissors" and computer == "paper":
        print("YOU WIN!!")
        player_score += 1

    elif player1 == "rock" and computer == "scissors":
        print("YOU WIN!!")
        player_score += 1

    elif player1 == computer:
        print("Its a draw")

    else:
        print(f"You lose!! Bot picked {computer}")
        computer_score += 1
        
    print(f"The score is {player_score} vs {computer_score}")

if player_score == 3:
    print("You win the seris")
    
elif computer_score == 3:
    print("The bot wins the series!")
else:
    print("Thanks for playing")