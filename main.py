name = input("What is your name? ")
u = name
p = u.capitalize()
playing = input(str("Do you want to play hangman " + p + "? ")).lower()
if playing != "yes":
    quit()
if playing == "yes":
    print("Alright")
random_word = list["help", "hello", "how", "hit", "howdy"]
tries = 6
#random_word = "help"
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
    if letters_guessed == letters_in_word:
        print("Correct!! You got the whole word!!")
        quit()
    if answer not in letters_in_word:
        tries -= 1
        print("Try again, you have " + str(tries) + " tries.")
    if answer in letters_in_word:
        print("You found a letter!!")
        if tries < 1:
            print("Your out of tries!")
            quit()
