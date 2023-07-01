'''
Mustafa Ali
Hangman
'''

game = ""

while game.upper() != "N":
        #MENU
    print("""
------------------------------

        PLAY HANGMAN?

    N - NO
    Y - YES
""")
    game = input()
    print("-"*30)

        #GAME - HANGMAN
    if game.upper() == "Y":        
        print("\n    Choose the phrase (Anything not alphanumerical will be visible)")
        daily = str(input())
        print("\n"*50)
        daily = daily.upper()
        dashy = dead = daily
        rainbow = dashy.maketrans("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ-", "------------------------------------ ")
        dashy = dashy.translate(rainbow)
        print(dashy)

        toDead = 8
        letters = []

        #daily will be typed by the Chooser.
        #dashy will be visible to the Guesser.
        #dead is to keep track of which letters have been guessed and need to be replaced.
        
        #The Guesser will guess the word one letter at a time.
        #First the Guesser will input a letter which will be stored as hmGuess.
        
        #If the letter is present in dead, the index of the letter will be found.
        #The index of the dash in dashy will be replaced with the letter in the index of dead.
        #Repeat until the letter is in all places in dashy.
        #If toDead is 0, the Guesser loses.

        while dashy != daily and toDead != 0:
            print("Now guess a letter!")
            hmGuess = str(input())
            hmGuess = hmGuess.upper()
            letterLoc = -2
            correct = True
            while letterLoc != -1:
                letterLoc = daily.find(hmGuess)
                if daily.find(hmGuess) != -1:
                    letterLoc = dead.find(hmGuess)
                if letterLoc == -1:
                    toDead -= 1
                    break
                if correct == True:
                    correct = False
                    toDead += 1
                dashy = dashy[:letterLoc] + hmGuess + dashy[letterLoc+len(hmGuess):]
                dead = dead[:letterLoc] + ("-" * len(hmGuess)) + dead[letterLoc+len(hmGuess):]
            letters.append(hmGuess)
            print("~"*40)
            print("So far, you guessed ", sorted(letters), "\nYou have ", str(toDead), " more chances.\n")
            print(dashy)
        if toDead == 0:
            print("Too bad, the word was", str(daily))
        else:
            print("Congrats, you win!")
    elif game.upper() != "N":
        print("That is not an option")
