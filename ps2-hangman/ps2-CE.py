# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check_letter = []
    for letter in secret_word:
        if letter not in letters_guessed:
            check_letter.append(False)
        else:
            check_letter.append(True)
    if False in check_letter:
        return False
    else:
        return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
            
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        available_letters.remove(letter)
    available_letters = ''.join(available_letters)
    
    return available_letters
       

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman. 
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.  
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!   
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = ""
    unique_letters = ""
    print("\nWelcome to the game Hangman! \n"
          "I am thinking of a word that is", len(secret_word), "letters long.")
    print(get_guessed_word(secret_word, letters_guessed))
    
    while guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("\tYou have", guesses_remaining, "guesses and", warnings_remaining, "warnings left. \n"
          "\tAvailable letters:", get_available_letters(letters_guessed),"\n"
          "----------------------------------------\n")
        guessed_letter = str.lower(input("Please guess a letter:"))
        
        if guessed_letter in letters_guessed or guessed_letter not in string.ascii_lowercase or len(guessed_letter) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                if guessed_letter in letters_guessed:
                    print("\tOops! You've already guessed that letter. You lose a warning.")                          
                else:
                    print("\tOops! That is not a valid letter. You lose a warning.")
            else:
                guesses_remaining -= 1
                if guessed_letter in letters_guessed:
                    print("\tOops! You've already guessed that letter.")
                else:
                    print("\tOops! That is not a valid letter.")
                print("\tYou have no more warnings so you lose a guess.")
               
        else:
            letters_guessed += guessed_letter
            if guessed_letter in secret_word:
                unique_letters += guessed_letter
                print("\tGood guess.")    
            elif guessed_letter in "aeiou":
                guesses_remaining -= 2
                print("\tOops! That vowel is not in my word.You lose 2 guesses.")  
            else:
                guesses_remaining -= 1
                print("\tOops! That consonant is not in my word.You lose 1 guess.")
        print(get_guessed_word(secret_word, letters_guessed)) 
        
    if is_word_guessed(secret_word, letters_guessed) == True:
        print("\nCongratulations, you won!"
              "\nYour total score for this game is", guesses_remaining * len(unique_letters))           
    else:
        print("\nUnlucky, you ran out of guesses. The word was", secret_word)
     

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    ''' 
    my_word = my_word.replace(' ','')
    compare_letter = []
    if len(my_word) == len(other_word):
        for i in range(len(other_word)):
            if my_word[i] == other_word[i] or my_word[i] == "_" and other_word[i] not in my_word:
                compare_letter.append(True)
            else:
                compare_letter.append(False)
        if False in compare_letter:
            return False
        else:
            return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = str()
    
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word)== True:
            possible_matches += other_word + " "
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)
        

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = ""
    unique_letters = ""
    print("\nWelcome to the game Hangman! \n"
          "I am thinking of a word that is", len(secret_word), "letters long.")
    print(get_guessed_word(secret_word, letters_guessed))
    print("To get a list of possible words, guess the character *.")
    
    while guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("\tYou have", guesses_remaining, "guesses and", warnings_remaining, "warnings left. \n"
          "\tAvailable letters:", get_available_letters(letters_guessed),"\n"
          "----------------------------------------\n")
        guessed_letter = str.lower(input("Please guess a letter:"))
        
        if guessed_letter == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
        
            if guessed_letter in letters_guessed or guessed_letter not in string.ascii_lowercase or len(guessed_letter) != 1:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    if guessed_letter in letters_guessed:
                        print("\tOops! You've already guessed that letter. You lose a warning.")                          
                    else:
                        print("\tOops! That is not a valid letter. You lose a warning.")
                else:
                    guesses_remaining -= 1
                    if guessed_letter in letters_guessed:
                        print("\tOops! You've already guessed that letter.")
                    else:
                        print("\tOops! That is not a valid letter.")
                    print("\tYou have no more warnings so you lose a guess.")
                   
            else:
                letters_guessed += guessed_letter
                if guessed_letter in secret_word:
                    unique_letters += guessed_letter
                    print("\tGood guess.")    
                elif guessed_letter in "aeiou":
                    guesses_remaining -= 2
                    print("\tOops! That vowel is not in my word.You lose 2 guesses.")  
                else:
                    guesses_remaining -= 1
                    print("\tOops! That consonant is not in my word.You lose 1 guess.")
            print(get_guessed_word(secret_word, letters_guessed)) 
            
    if is_word_guessed(secret_word, letters_guessed) == True:
        print("\nCongratulations, you won!"
                      "\nYour total score for this game is", guesses_remaining * len(unique_letters))           
    else:
        print("\nUnlucky, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
