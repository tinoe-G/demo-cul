#we are import a random module
import random


#random function
def name():
    #we pass a variable to store our value 0
    number_of_guesses = 0
    # we are using random randint from random module to choose a number
    number = random.randint(1, 10)

    #while loop will run until is less than 5 and break out of the loop
    while number_of_guesses < 5:
        guess = int(input("enter a guess :"))
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print(f'You guessed the number {number} in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))
name()
#I hope you enjoyed this game