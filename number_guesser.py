import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit();
else:
    print("please type a number")
    quit()



random_number  = random.randint(0,top_of_range)
guess = 0
print(random_number)

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number larger than 0")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
         print("you were below that")
    print("You got it wrong!")

print("You got it in", guess, "guesses")