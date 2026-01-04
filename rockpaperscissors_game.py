import random

def get_choices():
    player_choice=input("Enter your choice (rock, paper, scissors): ")
    options=['rock','paper','scissors']
    computer_choice=random.choice(options)
    choices={"player":player_choice, "computer": computer_choice}
    return choices

def get_winner(player,computer):
    print (f"You chose {player} , computer chose {computer}")
    if player == computer:
            return "Its a tie!"
    elif player := "rock":
        if computer == "scissors":
            return "rock smashes scissors, you Win!"
        else:
             return "paper covers rock, you lose!"
    elif player == "paper":
        if computer == "scissors":
            return "scissors cuts paper, you lose!"
        else:
             return "paper covers rock, you win!"
    elif player == "scissors":
         if computer == "rock":
            return "rock smashes scissors, you lose!"
         else:
              return "scissors cuts paper, you win!"
         
choices=get_choices()         
result = get_winner(choices["player"], choices["computer"])
print (result)

