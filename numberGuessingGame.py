#importing libraries
import random

#declaring variables
list = [1,2,3,4,5,6,7,8,9]
number = ""
chances = 9
guess = ""
#print(random.choice(number))

#game
while chances >= 5:
    number = random.choice(list)
    guess = int(input("Guess the Number: "))
    print(guess)
    if guess == number:
        print("Congratulations! You Won!")
        break
    else:
        print("That's not the number. Try again.")
        chances -= 1

    if chances == 4:
         print("You Lost. The Number is: ", number)