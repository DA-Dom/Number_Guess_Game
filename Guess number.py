import random

number_to_guess = random.randint(1 , 100)

while True:
    try:
        guess = int(input("Guess a number: "))

        if guess > number_to_guess:
            print("Too high")

        elif guess < number_to_guess:
            print("Too Low")

        else:
            print( "Thats the right number")
            break

    except:
        print(" Enter a valid number")
