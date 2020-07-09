# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str = ''
    for i in secret_word:
        if i in letters_guessed:
            str += i
        else:
            str += '_ '
    
    return str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str = ''
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            str += i
    return str
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    letters_guessed = list()
    warning = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print('Welcome to Hangman game!')
    print('This word have %d letters' % len(secret_word))
    
    while not is_word_guessed(secret_word, letters_guessed) and guesses >= 0:
        print('--------------------------')
        print('You have %d guess left' % guesses)
        print('Available letters: ' + get_available_letters(secret_word))
        c = input('Your guess: ')
        
        if c.isalpha(): # check alphabet
            if c not in letters_guessed: #  Check whether guessed or not!
                letters_guessed.append(c)
                if c in secret_word:
                    print('Nice!: ' + get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops!: ' + get_guessed_word(secret_word, letters_guessed))
                    if c in vowels:
                        guesses -= 2
                    else:
                        guesses -= 1
            else:
                warning -= 1
                if warning >= 0:
                    print('You have already guessed this letter. You have %d warnings left!: ' %warning + get_guessed_word(secret_word, letters_guessed))
                else:
                    print('You have no warning left, so you lose 1 guess: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            warning -= 1
            if warning >= 0:
                print('This is not valid letter. You have %d warnings left!: ' % warning + get_guessed_word(secret_word, letters_guessed))
            else:
                print('You have no warning left, so you lose 1 guess: ' + get_guessed_word(secret_word, letters_guessed))
    
    print('---*^*---')
    if guesses >= 0:
        print('You are best! Score: %d' % (guesses*len(secret_word)))
    else:
        print('Well well well, here is the word: ' + secret_word)
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    chk = my_word.replace(' ', '', my_word.count(' '))
    if len(chk) != len(other_word):
        return False
    
    for i in range(len(chk)):
        if chk[i] != '_' and chk[i] != other_word[i]:
            return False
    
    return chk.count('_') > 1



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_match = list()
    for i in wordlist:
        if match_with_gaps(my_word, i):
            list_match.append(i)
            
    if len(list_match) > 0:
        for i in list_match:
            print(i, end =' ')
    else:
        print('No matches found')



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    letters_guessed = list()
    warning = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print('Welcome to Hangman game!')
    print('This word have %d letters' % len(secret_word))
    
    while not is_word_guessed(secret_word, letters_guessed) and guesses >= 0:
        print('\n--------------------------')
        print('You have %d guess left' % guesses)
        print('Available letters: ' + get_available_letters(secret_word))
        c = input('Your guess: ')
        
        if c == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        
        if c.isalpha(): # check alphabet
            if c not in letters_guessed: #  Check whether guessed or not!
                letters_guessed.append(c)
                if c in secret_word:
                    print('Nice!: ' + get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops!: ' + get_guessed_word(secret_word, letters_guessed))
                    if c in vowels:
                        guesses -= 2
                    else:
                        guesses -= 1
            else:
                warning -= 1
                if warning >= 0:
                    print('You have already guessed this letter. You have %d warnings left!: ' %warning + get_guessed_word(secret_word, letters_guessed))
                else:
                    print('You have no warning left, so you lose 1 guess: ' + get_guessed_word(secret_word, letters_guessed))
        else:
            warning -= 1
            if warning >= 0:
                print('This is not valid letter. You have %d warnings left!: ' % warning + get_guessed_word(secret_word, letters_guessed))
            else:
                print('You have no warning left, so you lose 1 guess: ' + get_guessed_word(secret_word, letters_guessed))
    
    print('\n---*^*---')
    if guesses >= 0:
        print('You are best! Score: %d' % (guesses*len(secret_word)))
    else:
        print('Well well well, here is the word: ' + secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
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









# secret_word = 'apple'  
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_guessed_word(secret_word, letters_guessed)) 


# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_available_letters(letters_guessed))


# print(match_with_gaps("a_ _ le", "banana"))


show_possible_matches("a_ pl_ ")