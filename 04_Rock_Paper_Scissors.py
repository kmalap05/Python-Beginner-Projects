import random


def Game_Win(computer, player):
    if computer == player:
        return None
    elif computer == 'Rock':
        if player == 'Scissors':
            return False
        elif player == 'Paper':
            return True
    elif computer == 'Paper':
        if player == 'Rock':
            return False
        elif player == 'Scissors':
            return True
    elif computer == 'Scissors':
        if player == 'Rock':
            return True
        elif player == 'Paper':
            return False


def Play_Again():
    play = ["Yes", "No"]
    response = None
    while response not in play:
        response = input("Play Again? (Yes/No): ").capitalize()
    if response == 'Yes':
        return True
    else:
        return False


while True:
    choices = ['Rock', 'Paper', 'Scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors?: ").capitalize()

    print(f"Computer: {computer}")
    print(f"Player: {player}")

    result = Game_Win(computer, player)
    if result == None:
        print("Tie!")
    elif result:
        print("You Win!")
    else:
        print("You Lose!")

    play_again = Play_Again()
    if play_again == False:
        break

print("Byeeeeeeeeeeee!")
