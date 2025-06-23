# Rock Paper Scissors game between user and system
import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors Game!")
total_rounds = int(input("Enter the number of rounds you want to play: "))

user_score = 0
system_score = 0

for round_num in range(1, total_rounds + 1):
    print(f"\n--- Round {round_num} ---")
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in options:
        print("Invalid choice. Round forfeited.")
        system_score += 1
        continue

    system_choice = random.choice(options)
    print("System chose:", system_choice)

    if user_choice == system_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and system_choice == "scissors") or \
         (user_choice == "paper" and system_choice == "rock") or \
         (user_choice == "scissors" and system_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("System wins this round!")
        system_score += 1

# Final Score Display
print("\n===== Game Over =====")
print("Your score:", user_score)
print("System score:", system_score)

if user_score > system_score:
    print("Congratulations! You won the game!")
elif user_score < system_score:
    print("System wins the game. Better luck next time!")
else:
    print("It's a tie game!")

