from random import randint
import sys

hangman = ['''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["abruptly",
             "abruptly",
             "abruptly"]

selected_word = word_list[randint(0, 2)]
letter_list = list(selected_word)
error_counter = 0
guess_list = ["_" for x in range(len(letter_list))]
print(guess_list)

while error_counter < 7:
    guessed_letter = input("Guess a letter in the word")
    if not guessed_letter.isalpha():
        print("Please enter only one alphabetical characters")
        continue

    elif len(guessed_letter) > 1:
        print("Please enter only one alphabetical characters")
        continue

    elif guessed_letter not in letter_list:
        if error_counter == 6:
            print("Sorry You lost :(")
            sys.exit()
        error_counter += 1
        print(hangman[error_counter])

    elif guessed_letter in letter_list:
        for n, i in enumerate(letter_list):
            if i == guessed_letter:
                print(n)
                guess_list[n] = guessed_letter
                print(guess_list)
                if "_" not in guess_list:
                    print("Congrats! You won!")
                    sys.exit()
                continue


