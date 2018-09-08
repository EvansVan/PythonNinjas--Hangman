#secret word
word = 'EVAPORATE'

#empty value to assign values to
global guesses
guesses = []

global correct
correct = 0


while correct<9:
    print('Do you really need a clue?? When water changes state from liquid to gas.')

    guess = input(str('Enter only one letter please: '))

    tries = guess.upper()

    #checks ifthe input matches previous input
    if guess in guesses:
        print("You have already entered this letter")
    else:
    #ensures user input is limited to one lettter        
        if len(guess) > 1:
            print('Please enter one value')
        #checks for entry of blank or no value
        elif len(guess)<1:
            print('Blank spaces are not valid')
        #checks for incorrect guess
        elif tries not in word:        
            print('incorrect')
        #loop to check for values in the word
        else: 
            for char in word:
                if char in tries:
                    print(char, end="")
                    guesses.append(guess)
                    correct += 1
                else:
                    print('_',end="")
                    
    print('\n')
    #my test to check for saved values
    #print(guesses)
print('Congratulations you got the word correct the word is ' + word)                    
                    
