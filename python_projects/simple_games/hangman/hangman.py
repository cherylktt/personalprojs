import random


def hangman():

    list = ["escape", "shout", "outfit", "jail", "humanity",
            "ferry", "pass", "star", "perform", "speech"]
    word = random.choice(list)
    validLetters = "abcdefghijklmnopqrstuvwxyz"

    turns = 10
    guessmade = " "

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You win!")
            print("Play again? Y/N")
            if input() == "Y":
                hangman()
            else:
                break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character.")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |         ")
                print("  |         ")
                print("  |         ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |    0    ")
                print("  |         ")
                print("  |         ")
                print("  |         ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |    0    ")
                print("  |    |    ")
                print("  |         ")
                print("  |         ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |    0    ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |         ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |    0    ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |   /     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |    0    ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |   / \   ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("  |         ")
                print("  |  \ 0    ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |   / \   ")
            if turns == 1:
                print("1 turn left")
                print("  --------  ")
                print("  |         ")
                print("  |  \ 0 /  ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |   / \   ")
            if turns == 0:
                print("You lose. Game over.")
                print("  --------  ")
                print("  |    |    ")
                print("  |  \ 0 / ")
                print("  |    |    ")
                print("  |    |    ")
                print("  |   / \   ")
                print("Play again? Y/N")
                if input() == "Y":
                    hangman()
                else:
                    break


print("Let's play hangman! Try to guess the word in less than 10 attempts.")
hangman()
print()
