import random
user = False

while user == False:
    print("Let us play rock, paper and scissors!")
    user = (input())
    computer = random.choice(["Rock", "Paper", "Scissors"])
    print(computer)

    if user == computer:
        print("Draw!")
    elif user == "Rock":
        if computer == "Paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user == "Paper":
        if computer == "Rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user == "Scissors":
        if computer == "Rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid play, check your spelling!")
    user = False
