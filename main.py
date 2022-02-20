name = input("What is your name? ")
name_upper = name.capitalize()
playing = input(str("Do you want to play hangman " + name_upper + "? ")).lower()
if playing != "yes":
    quit()
if playing == "yes":
    print("Alright")
#random_word = list["help", "hello", "how", "hit", "howdy"]
tries = 6
mode = input("Do you want to play easy(8 tries), medium(6 tries), or hard(4 tries)? ").lower()
if mode == 'easy':
    tries += 2
if mode == 'hard':
    tries -= 2
else:
    tries
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
    if tries == 1:
        print("Your out of tries!")
        quit()
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
        print("The letter " + answer.upper() + " was correct!!!")
