'''
Made by Swastik Kakran on 27 March 19:52
Must follow GitHub: https://www.github.com/kakranswastik

Have fun playing!!!
'''
import random
import string
from visual import lives_visual_dict
from words import words

def Vaild_word(words):          #Gets a valid word from list words without - or empty space
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word =  Vaild_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7       #number of chances in game
    #Getting user input

    while len(word_letters) > 0 and lives > 0:
        print('\nYou have ', lives, 'lives left. You have choosed these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives-=1
                print('\nYour letter', user_letter, 'is not in the word. Choose another letter.')

        elif user_letter in used_letters:
            print('\nYou have already choosed this letter. Please choose another one.')

        else:
            print('Enter a valid letter!')

    #when lives run out or word letters run out, program reaches here
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You lost! The word was ", word, " Better luck next time...")

    else:
        print("YAY you guessed the right word. It was ", word)

if __name__=='__main__':
    hangman()