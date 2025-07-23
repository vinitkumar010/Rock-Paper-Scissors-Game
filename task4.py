import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user = input("Choose rock, paper, or scissors: ").lower()

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue

        computer = get_computer_choice()
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        winner = get_winner(user, computer)

        if winner == "tie":
            print("It's a tie! 🤝")
        elif winner == "user":
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏁 Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 You are the overall winner!")
            elif user_score < computer_score:
                print("💻 Computer wins overall!")
            else:
                print("It's a tie overall! 🤝")
            break

        round_number += 1

# Run the game
play_game()
