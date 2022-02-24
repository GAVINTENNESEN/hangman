import random

name = input("What is your name? ")
name_upper = name.capitalize()
playing = input(str("Do you want to play hangman " + name_upper + "? ")).lower()
if playing != "yes":
    quit()
if playing == "yes":
    print("Alright")

# Get word list
random_word_list = list()
with open(file='Words.txt', mode='r') as f:
    data = f.readlines()
    for row in data:
        random_word_list.append(row.strip('\n'))

tries = 6
mode = input("Do you want to play easy(8 trie"
             "), medium(6 tries), or hard(4 tries)? ").lower()
if mode == 'easy':
    tries += 2
elif mode == 'hard':
    tries -= 2
random_word = random_word_list[random.randint(0, len(random_word_list))]
answer = None
letters_in_word = list(random_word)
letters_guessed = list()
while answer != random_word:
    answer = input("Guess a letter: ")
    if len(answer) > 1:
        print("Too many letters!!!  Try again!")
        continue
    letters_guessed.append(answer)
    if tries == 1:
        print("Your out of tries, the word was " + random_word.upper() + ".")
        quit()
    # visible word will be used to track the whole state of the word so it can be printed at one shot
    visible_word = ''
    for letter in letters_in_word:
        if letter in letters_guessed:
            visible_word += letter
        else:
            visible_word += '_'
    print(visible_word)
    # whole word is used to see if we've matched the whole word or not
    whole_word = True
    for letter in letters_in_word:
        if letter not in letters_guessed:
            whole_word = False
    if whole_word:
        print("Correct!! You got the whole word!!")
        quit()
    if answer not in letters_in_word:
        tries -= 1
        print("Try again, you have " + str(tries) + " tries.")
    if answer in letters_in_word:
        print("The letter " + answer.upper() + " was correct!!!")
