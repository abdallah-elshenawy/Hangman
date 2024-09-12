import random
words = ["ali", "karem", "isaq", "kamel", "nader"]
rand_word = random.choice(words)
displays = ['_'] * len(rand_word)
print(" ".join(displays))
Hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

chances = 6
print(Hangman[6 - chances])
exist_list = []

while ('_' in displays and chances > 0):
   guessed = input("Guess a letter: ").lower()
   if (guessed in exist_list):
      print("You guessed this letter before")
   elif (guessed not in rand_word):
      chances -= 1
      print(Hangman[6 - chances])
   else:
      for index in range(len(rand_word)):
         if (guessed == rand_word[index]):
            displays[index] = rand_word[index]

   print(" ".join(displays))
   exist_list.append(guessed)
   print(f"You have only {chances} more tries\n")

if (chances == 0):
   print("""   
   *** GAME OVER ***
""")
else:
   print("""
   *** You Win !! ***
""")
