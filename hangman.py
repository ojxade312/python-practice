import random
def Welcome():
    # define name variable
    name = input(""" >Hi! Welcome to CyberHangman. Please enter your name: <""")
    if name.isAlpha() == True:
        print (""" Hi """,name,""" """)
    else:
         print ("Please use your name with no numbers")

def Play_again():
    response = input("Would you like to play again. Enter Y for yes and N for no").lower()
    if response == "y":
        game_run()
    else:
        print("Thanks for playing ! See you next time")

def get_word():
    words = ["python", "barbie", "sprinkles", "sparkles", "kisses"]
    return random.choice(words).lower()

def game_run():
    # run game
    Welcome()
    #define alphabet
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    #random word generator
    word = get_word()
    #e,pty list for guessed letters
    letters_guessed = []
    #tries variable
    tries = 7
    #set inital guess to false
    guessed = False
    #print empty line
    print()
    #print guess hints
    print("The word contains, len(word), 'letters.")
    print(len(word) * '_')

    while guessed == False and tries > 0:
        print('You have' + str(tries) + ' tries')
        guess = input ('Guess a letter in the word or enter the full word.').lower()
        #user imputs letter
        if len(guess) ==1:
            if guess not in alphabet:
                print('Enter a letter not a number')
            elif guess in letters_guessed:
                print ('You have already guessed that, try again')
            elif guess not in word:
                print('Sorry, that letter is not part of the word:(')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Great, that letter exists in that word !')
            else:
                print('Check again, you may have entered the wrong entry')

        #user inputs full word
        elif len(guess) == len(word):
            if guess == word:
                print('Great job! You guessea the word correctly!')
                guessed = True
            else:
                print('Sorry, that was not the word we are looking for')
                tries -=1

        else:
            print('The length of your guess is not the same as the length of the correct word.')
            tries -=1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status+= letter
                else:
                    status += '_'
            print(status)

        if status == word:
            print('God Job! You have guessed the word correctly!')
            guessed = True
        elif tries ==0:
            print("Opps! You ran out of guesses and you couldn't guess the word")

    Play_again()

game_run()