import random

name = input("What is your name? ")
name_upper = name.capitalize()
playing = input(str("Do you want to play hangman " + name_upper + "? ")).lower()
if playing != "yes":
    quit()
if playing == "yes":
    print("Alright")
random_word_list = list(["help", "hello", "how", "hit", "howdy"])
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
    visible_word = ''
    for letter in letters_in_word:
        if letter in letters_guessed:
            visible_word += letter
        else:
            visible_word += '_'
    print(visible_word)
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
