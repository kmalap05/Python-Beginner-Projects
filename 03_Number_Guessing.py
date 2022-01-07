import random


def Game_Winner(computer, player):
    if computer == player:
        print("You Won!")
        return "You Won!"
    elif player > computer:
        return "Guess Less Number!"
    elif player < computer:
        return "Guess Large Number!"


def play_again():
    playagain = ['Yes', 'No']
    response = None
    while response not in playagain:
        response = input("Play Again (Yes/No): ").capitalize()
        if response == 'No':
            exit()


if __name__ == '__main__':
    computer = random.randint(1, 101)
    print("Computer : " + str(computer))
    while True:
        # print(f"Computer: {computer}")
        try:
            player = None
            player = int(input("Guess Number(1 to 100): "))
        except ValueError:
            print("Enter Number Only!")

        if player in range(1, 101):
            result = Game_Winner(computer, player)
            if result == "You Won!":
                play_again()
            elif result == "Guess Less Number!":
                print(f"Guess Small Number Than {player}!")
            elif result == "Guess Large Number!":
                print(f"Guess Big Number Than {player}!")
