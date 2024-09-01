import random
words = ["ali", "karem", "isaq", "kamel", "nader"]
 
# choosing a random word
rand_word = random.choice(words)

# the spaces of the rand word
displays = ["_"] * len(rand_word)

# the list of the exist letters
exist_list = []

hangman = ["""          
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""","""          
   +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""", """
   +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""", """
   +---+
  |   |
  O   |
 /    |
      |
      |
=========
""", """
   +---+
  |   |
  O   |
      |
      |
      |
=========
""", """
   +---+
  |   |
      |
      |
      |
      |
=========
""", """
   +---+
      |
      |
      |
      |
      |
=========
"""]
chances = 6
print(" ".join(displays))
print(hangman[6])
while ("_" in displays) and (chances != 0):
   guessed = input("Please guess a letter: ")
   if guessed in exist_list:
      print("\nYou already guessed that. Try again.")
   elif (guessed not in rand_word):
      chances -= 1
      print(hangman[chances])
   else:
      for index in range(len(rand_word)):
         if (guessed == rand_word[index]):
            displays[index] = guessed
            break
      
   print(" ".join(displays))
   print(f"You have {chances} more tries.")
   exist_list.append(guessed)
      