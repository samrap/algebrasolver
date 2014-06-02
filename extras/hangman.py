import os
import sys
import time
import random

"""Sam Rapaport's Hangman Game.

I wrote this game in probably less than 30 minutes,
so I wouldn't doubt if there are logic errors or an
easier way to do this.
"""

hangman = [

"""
  *---*
  |   |
      |
      |
      |
      |
=========
""",

"""
  *---*
  |   |
  O   |
      |
      |
      |
=========
""",

"""
  *---*
  |   |
  O   |
  |   |
      |
      |
=========
""",

"""
  *---*
  |   |
  O   |
  |\  |
      |
      |
=========
""",

"""
  *---*
  |   |
  O   |
 /|\  |
      |
      |
=========
""",

"""
  *---*
  |   |
  O   |
 /|\  |
   \  |
      |
=========
""",

"""
  *---*
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

]

def clear(numlines=120):
    """Clear the screen of all output.
    numlines is an optional fallback parameter.
    Credit to Jon Cage on SO for answering someone's
    question about this.
    """

    # Unix, OSX, Linux
    if os.name == 'posix':
        os.system('clear')

    # DOS/Windows
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('CLS')

    # Fallback
    else:
        print '\n' * numlines

def chooseLevel():
    print ''
    print "HANGMAN V1.0"
    print "There are two difficulties to choose from:"
    print ''
    print "'Normal' is a list of 500 of the most common English words"
    print "'Insanity' is a list of every word in the English language"

    level = ''
    while level != 'insanity' and level != 'normal':
        level = raw_input("Enter the difficulty: ").lower()
    return level

def setLevel(level):
    dictionary = open('./extras/%s' % level, 'r')
    rawlist = dictionary.readlines()
    wordlist = [word.upper().replace('\n', '') for word in rawlist]
    dictionary.close()

    return wordlist

def randomWord(words):
    index = random.randrange(0, len(words))
    print "A random word has been chosen. You get 7 wrong guesses."
    time.sleep(1.5)
    sys.stdout.write("Get ready")
    for _ in xrange(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    return words[index]

def checkWin(blanks):
    if any(b == '_' for b in blanks):
        return False
    return True

def mainLoop(w):
    guesses = 0
    no = []
    blanks = ['_']*len(w)
    w = list(w)

    while guesses < len(hangman):
        clear()
        print ''
        print "Letters guessed: {}".format(', '.join(no))
        print hangman[guesses]
        print ''
        print 'Word: ' + ' '.join(blanks)

        letter = raw_input("Guess a letter: ").upper()
        if letter in w:
            for index, obj in enumerate(w):
                if obj == letter:
                    blanks[index] = letter

            if checkWin(blanks) is True:
                break;
        else:
            print "Wrong guess!"
            time.sleep(2)
            no.append(letter)
            guesses += 1
    else:
        print "You lose!"
        print "The word was " + ''.join(w)
        return True

    print "You won!"
    print "The word was " + ''.join(w)


def playHangman():
    clear()
    level = chooseLevel()
    wordlist = setLevel(level)
    word = randomWord(wordlist)
    mainLoop(word)

if __name__ == '__main__':
    playHangman()
