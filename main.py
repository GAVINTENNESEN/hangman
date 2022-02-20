name = input("What is your name? ")
u = name
p = u.capitalize()
playing = input(str("Do you want to play hangman " + p + "? ")).lower()
if playing != "yes":
    quit()
if playing == "yes":
    print("Alright")
#random_word = list["help", "hello", "how", "hit", "howdy"]
random_word = "help"
answer = None
letters_in_word = list(random_word)
letters_guessed = list()
while answer != random_word:
    answer = input("Guess a letter: ")
    if len(answer) > 1:
        print("Too many letters!!!  Try again!")
        continue
    letters_guessed.append(answer)
    for letter in letters_in_word:
        if letter in letters_guessed:
            print(letter)
        else:
            print('_')
    if answer == random_word:
        print("Correct!! You got the whole word!!")
    if answer != letters_in_word:
        print("Try again")
        if answer == letters_in_word:
            print("You found a letter!!")
