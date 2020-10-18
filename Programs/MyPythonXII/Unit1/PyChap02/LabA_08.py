# File name: ...\\MyPythonXII\Unit1\PyChap02\LabA_08.py
# Word Jumble game
import random
# create a sequence of words to choose from
WORDS = ("Python", "Cobol", "Pascal", "C++", "Java", "Visual Studio", "MySql", "Fortran")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# Create a variable to use later to see if the guess is correct
correct = word
correct = correct.lower()

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print \
("""
\t\t    Welcome to Word Jumble Game!
\t\t----------------------------------
\t\t----Guess a Computer Language-----
\tUnscramble the letters to make a word.
   (Note. Press the enter key at the prompt to quit.)
""")
print ("The jumble word is:", jumble)
guess = input("\nPlease enter again your guess: ")
while (guess != correct) and (guess != ""):
    print ("Sorry, %s is not exactly the jumble word" %jumble)
    guess = input("Please enter again your guess: ")
    guess = guess.lower()

if guess == correct:
    print ("That's it! You guessed it!\n")

print ("Thanks for playing.")

