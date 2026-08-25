import random

print("💭Welcome to the Number Guessing Game💭")
print("You have 3 chances to guess a randomly generated number between 1-10")
print(" ")
number = random.randint(1, 10)
for i in range(3):
    guess_number= int(input("Guess a number between 1 to 10: "))
    if number == guess_number:
        print("🎉🎉You guessed correctly!!🎉🎉")
        break
    elif number > guess_number:
        print("Your number is too small 😢")
    elif number < guess_number:
        print("Your number is too large 😬")
else:
    print("Oh No! You loose 😔")
