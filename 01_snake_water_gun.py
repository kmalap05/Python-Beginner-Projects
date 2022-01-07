import random


def Game_Win(computer, player):
    if computer == player:
        return None
    elif computer == 'Snake':
        if player == 'Water':
            return False
        elif player == 'Gun':
            return True
    elif computer == 'Water':
        if player == 'Gun':
            return False
        elif player == 'Snake':
            return True
    elif computer == 'Gun':
        if player == 'Water':
            return True
        elif player == 'Snake':
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
    choices = ['Snake', 'Water', 'Gun']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Snake, Water or Gun?: ").capitalize()

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
