import random

print("Welcome to my no guessing game!")

lower_range = int(input("enter lower range: "))
upper_range = int(input("enter upper range: "))

target = random.randint(lower_range,upper_range)

total_guess = 7
guess_counter = 0

while total_guess > guess_counter:
    your_guess = int(input("guess a number: "))
    
    if your_guess == target:
        print("Great! you guessd it right")
        print(f"You attempted {guess_counter} times")
        break

    elif your_guess >= target:
        print("Ops! too highh! try again :)")

    elif your_guess <= target:
        print("sry too low, try again")
    
    guess_counter += 1

if guess_counter == total_guess and your_guess != target:
    print(f' You Lost:( {target} was the number')

