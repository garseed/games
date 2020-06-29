actress = "Amy Adams"
actress_input = str(input("Enter an actor: ")).title()
amy_adams_filmography1 = ("Arrival", "2016")
amy_adams_filmography2 = ("Enchanted", "2007")
amy_adams_filmography3 = ("American Hustle", "2013")
amy_adams_filmography4 = ("Doubt", "2008")
incorrect_guess_count = 0
incorrect_guess_limit = 3
correct_guess_count = 0
correct_guess_limit = 4

if actress_input == actress:
    print("You have 3 chances to guess the four films \nAmy Adams is known for according to IMDb.\n3 incorrect guesses and you're out!")
else:
     print("Dylan only programmed Amy Adams into this \nbuy The Last of Us Part 2 if you want a real game")
     quit()

guess_1 = str(input("Enter your first guess: ")).title()
if guess_1 == amy_adams_filmography1[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_1 == amy_adams_filmography2[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_1 == amy_adams_filmography3[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_1 == amy_adams_filmography4[0]:
    print("Correct!")
    correct_guess_count += 1
else:
    print("Incorrect!")
    incorrect_guess_count +=1

guess_2 = str(input("Enter your next guess: ")).title()

if guess_2 == amy_adams_filmography1[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_2 == amy_adams_filmography2[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_2 == amy_adams_filmography3[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_2 == amy_adams_filmography4[0]:
    print("Correct!")
    correct_guess_count += 1
else:
    print("Incorrect!")
    incorrect_guess_count +=1

guess_3 = str(input("Enter your next guess: ")).title()
if guess_3 == amy_adams_filmography1[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_3 == amy_adams_filmography2[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_3 == amy_adams_filmography3[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_3 == amy_adams_filmography4[0]:
    print("Correct!")
    correct_guess_count += 1
else:
    print('Incorrect!')
    incorrect_guess_count +=1

if incorrect_guess_count == incorrect_guess_limit:
    print("3 strikes, you're out! Sorry you're straight")
    quit()
else:
    pass

guess_4 = str(input("Enter your next guess: ")).title()
if guess_4 == amy_adams_filmography1[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_4 == amy_adams_filmography2[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_4 == amy_adams_filmography3[0]:
    print("Correct!")
    correct_guess_count += 1
elif guess_4 == amy_adams_filmography4[0]:
    print("Correct!")
    correct_guess_count += 1
else:
    print('Incorrect!')
    incorrect_guess_count +=1

if incorrect_guess_count == incorrect_guess_limit:
    print("3 strikes, you're out! Sorry you're straight")
    quit()
else:
    pass

if correct_guess_count == correct_guess_limit:
    print("You did it! Congrats on being gay!")
    quit()
else:
    pass


guess_5 = str(input("Enter your next guess: ")).title()
if guess_5 == amy_adams_filmography1[0]:
    print("Correct!")
    correct_guess_count += 1

elif guess_5 == amy_adams_filmography2[0]:
    print("Correct!")
    correct_guess_count += 1

elif guess_5 == amy_adams_filmography3[0]:
    print("Correct!")
    correct_guess_count += 1

elif guess_5 == amy_adams_filmography4[0]:
    print("Correct!")
    correct_guess_count += 1

else:
    print('Incorrect!')
    incorrect_guess_count += 1

if incorrect_guess_count == incorrect_guess_limit:
    print("3 strikes, you're out! Sorry you're straight")
    quit()
else:
    pass
if correct_guess_count == correct_guess_limit:
    print("You did it! Congrats on being gay!")
    quit()
else:
    pass

guess_6 = str(input("Enter your next guess: ")).title()
if guess_6 == amy_adams_filmography1[0]:
    print("You did it! Congrats on being gay!")
elif guess_6 == amy_adams_filmography2[0]:
    print("You did it! Congrats on being gay!")
elif guess_6 == amy_adams_filmography3[0]:
    print("You did it! Congrats on being gay!")
elif guess_6 == amy_adams_filmography4[0]:
    print("You did it! Congrats on being gay!")
else:
    print("3 strikes, you're out! Sorry you're straight")
