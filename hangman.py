
import random

def getword(namefile):   # function getword with namefile parameter will try read file word and return content of file if system don't have file will return 0
    try:
        f = open(namefile, "r")
        return f.read()
    except:
        return 0



def startGame(listword):
    word = random.choice(listword)
    word = word.upper()
    so_far = "-" * len(word) # one dash for each letter in word to be guessed

    wrong = 0 # counter to keep track of number of wrong guesses

    used = [] # list to keep track of letters already guessed
    letterwin = 0  # count the number of correctly guessed words

    print("Welcome to Hangman. Good luck!")
    winword = 0 # test variable when the player guesses the whole word incorrectly
    while wrong < 5 and so_far != word and winword == 0: 
        option = 2 # when start, option always is 2 for the user to enter each character
        # if the number of correctly guessed letters is half of the word, then we can have the user predict the whole word
        if (letterwin == int(len(word)/2)+1):
            print ("\nHere is your puzzle:\n", so_far)
            option = input("You guessed half of the letters in the puzzle correctly, you have 2 option:\n 1. Enter 1 if you want to guess the word, if it is correct you win, if you guess wrong you lose. \n 2. Enter 2 if you want keep guessing each letter \n Enter your option: \t")
            while option not in ['1','2']:  # check if user enter number is not 1 or 2, let the user re-enter
                option = input("You guessed half of the letters in the puzzle correctly, you have 2 option:\n 1. Enter 1 if you want to guess the word, if it is correct you win, if you guess wrong you lose. \n 2. Enter 2 if you want keep guessing each letter \n Enter your option: \t")
        if option == '1': # if option is 1, let the user guess the whole word
            wordguess = input("Enter word you guess:")
            if wordguess != word: # If the user guesses wrong, the game ends
                winword = 1
            else:  # else user win
                so_far = word
        else:  # if option is 2, keep letting the user predict each letter

            print ("You currently have ",wrong," incorrect guesses.")
            print ("\nHere is your puzzle:\n", so_far)

            guess = input("Please enter your guess:\n")
            guess = guess.upper()
            while len(guess) != 1:  # check guess letter of user, if they guess 2 or more letters, have them re-enter
                print("Please enter one letter!")
                guess = input("Please enter your guess:\n")
                guess = guess.upper()

            while guess in used: # check if the user has already entered that letter then have them re-enter it
                print ("You have guessed the letter:\t", guess)
                guess = input("Enter your guess again:\t")
                guess = guess.upper()

            used.append(guess) # add the new letter, user entered to the list of characters entered by the user

            if guess in word:
                letterwin += 1
                print ("Congratulations, you guessed a  letter ", guess, " is in the puzzle! \n")

                # create a new so_far to include guess if user correct prediction
                new = ""


                for i in range(len(word)):
                    if guess == word [i]:
                        new += guess
                    else:
                        new += so_far [i]
                so_far = new

            else:
                print ("\nSorry, that letter ", guess, "isn't in puzzle")
                wrong += 1
    if winword == 1: # if winword = 1, then the user guesses the wrong keyword
        print("Sorry, you guessed the wrong keyword, \n The correct word was ",word)

    if wrong == 5: # wrong =5, user guesses wrong 5 times
        print ("Sorry, you have 5 incorrect guesses, you lose.\n The correct word was ",word)

    else:
        print("\nCongratuations, You got the correct word, ", word)





namefile = input("What file stores the puzzle words? \n")
words = getword(namefile) 
while words == 0: # if words = 0, means the file cannot be read or the file does not exist, let the user re-enter the file
    print("We can't find any such files")
    namefile = input("What file stores the puzzle words? \n")
    words = getword(namefile)
listword = words.split(",") # get list word 
while True: # Repeat the game until the player no longer wants to play
    play = input("Would you like to play hangman (yes, no)? \n")
    while play not in ['yes','no','YES','NO']: # check if user enter is not yes or no, let user re-enter
        play = input("Sorry, you only need enter (yes, no), would you like to play hangman (yes, no)? \n")
    if play == 'no' or play ==' NO': 
        print("Thank for playing!")
        break
    else:
        startGame(listword)
