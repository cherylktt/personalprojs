import random
number = random.randint(0, 20)
number_of_guesses = 0

print('Hello, welcome to the guessing game. To begin, choose an integer from 0 to 20: ')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Too low!')
    if guess > number:
        print('Too high!')
    if guess == number:
        break
if guess == number:
    print('Correct! You guessed the number in '
          + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number. The number was ' + str(guess) + '.')
