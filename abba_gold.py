
abba_input = str(input("It's never a bad time to listen to the 1992 ABBA greatest hits compilation ABBA Gold."
                       "\nI'll help you decide which track to put on"
                       "\nAre you"
                       "\nGay"
                       "\nor"
                       "\nStraight ")).title()
gay = "Gay"
straight = "Straight"
happy = "Happy"
sad = "Sad"
single = "Single"
taken = "Taken"
depressed = "Depressed"
horny = "Horny"
if abba_input == straight:
    print("I'm sorry to hear that."
          "\nPut on track 15 'Does Your Mother Know',"
          "\nthe only song on the record with lead vocals by the men of ABBA. "
          "\nHave fun playing this off of your Android phone while admiring your Funko Pops")
    quit()
else:
    print("Oh thank god")

abba_input = str(input("Okay, now that it's just us girls,"
                       "\nhow are you feeling today sis?"
                       "\nHappy"
                       "\nor"
                       "\nSad ")).title()

if abba_input == happy:
    happy_abba = str(input("Are you"
                           "\nSingle"
                           "\nor"
                           "\nTaken ")).title()
    if happy_abba == single:
        print("Put on Track 1, 'Dancing Queen' "
              "\nand realize that"
              "\nwhile we respect and stan Robyn"
              "\nnone of her songs will ever achieve the euphoria"
              "\nachieved in 'Dancing Queen.")
        quit()
    else:
        print("Put on Track 6 'Super Trooper' "
              "\nand try to convince your"
              "\nsignificant other to do the choreo"
              "\nfrom the end of Mamma Mia Here We Go Again. ")
        quit()
else:
    sad_abba = str(input("But are you actually"
                         "\nHorny"
                         "\nor"
                         "\nDepressed ")).title()
    if sad_abba == horny:
        print("Put on track 14, 'Gimme! Gimme! Gimme!'"
              "\nand go masturbate on the couch for the "
              "\nfifth time today you pervert")
        quit()
    else:
        print("Put on track 8, 'The Winner Takes It All' "
              "\n and stare out the window, mixed drink in hand"
              "\nand wonder where it all went wrong")
        quit()