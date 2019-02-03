import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for c in secretWord:
        if not(c in lettersGuessed):
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    g=''
    for c in secretWord:
        if not(c in lettersGuessed):
            g=g+'_'
        else:
            g=g+c   
    return g
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    s=''
    for letter in string.ascii_lowercase:
        if not(letter in lettersGuessed):
            s=s+letter
    return s
 # FILL IN YOUR CODE HERE...
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long")
    print("-----------")
    mistakesMade = 0
    lettersGuessed=[]
    while mistakesMade<8:
        print("You have "+ str(8-mistakesMade)+" guesses left")
        print("Available Letters :"+ str(getAvailableLetters(lettersGuessed)))
        a=input("Please guess a letter: ")
        if(len(a)==1) and not(a in lettersGuessed):
            a.lower()
            lettersGuessed.append(a)
        else:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            continue
        if(a in secretWord):
            print("Good Guess: "+ getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessed))
            mistakesMade+=1
        print("-----------")
        if(isWordGuessed(secretWord, lettersGuessed)):
            print("Congratulations, you won!")
            break
        
    if(mistakesMade>=8):
        print("Sorry, you ran out of guesses. The word was "+ secretWord)

secretWord = chooseWord(WORDLIST_FILENAME).lower()
hangman(secretWord)
