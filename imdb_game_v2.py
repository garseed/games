actress = "Amy Adams"
amy_adams_filmography = ["Enchanted", "Doubt", "American Hustle", "Arrival"]
incorrect_guess_limit = 0
correct_guess_limit = 0

actress_input = str(input("Enter an actor: ")).title()
if actress_input == actress:
    print("You have 3 chances to guess the four films "
      "\nAmy Adams is known for according to IMDb."
      "\n3 incorrect guesses and you're out!")
else:
    print("I only programmed this for Amy Adams, I'm still dumb as shit.")
    quit()
while incorrect_guess_limit < 3:
    guess = str(input("Enter a movie: ")).title()
    if guess in amy_adams_filmography:
        print("Correct")
        correct_guess_limit += 1
        if correct_guess_limit == 4:
            print("You did it!")
        else:
            pass
    else:
        print("Incorrect!")
        incorrect_guess_limit += 1

else:
    print("you failed")