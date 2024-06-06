# Rock, Paper, Scisscors

import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    win_text = "player win"
    lose_text = "player lose"

    print(f"player chose {player}, computer chose {computer}")

    if player == computer:
        return "it's a tie!"
    elif player == "paper":
        if computer == "rock":
            return win_text
        else:
            return lose_text
    elif player == "rock":
        if computer == "scissors":
            return win_text
        else:
            return lose_text
    elif player == "scissors":
        if computer == "paper":
            return win_text
        else:
            return lose_text

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)