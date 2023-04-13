
# A guessing game where user guesses a random number between 1 and 10

# First we have to import random 
import random

# Next we assign the random number to a variable called secret_number
secret_number = random.randint(1 ,10)

# Now we include the user's input which we assign to another variable


# Then we check to ensure the random number and user's number match using if statements and use a while loop to keep receiving
# the user's input as many times as we wish
while True:
    user_number = int(input("Please choose a number between 1 and 10: "))
    if user_number == secret_number:
        print("Congratulations")
        break
    elif user_number > secret_number:    
        print ("Too high")
    elif user_number < secret_number:
        print ("Too Low")

            

'''
import random

# Generate a random number between 1 and 10 (inclusive)
random_number = random.randint(1, 10)

# Ask the user to guess the number
print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
guess = int(input())

# Keep asking the user to guess the number until they get it right
while guess != random_number:
    if guess < random_number:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
    guess = int(input())

# If the user guessed the number correctly, congratulate them!
print("Congratulations! You guessed the number correctly.")
'''


 

