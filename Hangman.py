name = "noppanut"
trial = 5

guessed_letters = set()


while trial > 0:
    letter = str(input("Guess letter: "))

    if letter in name:
        guessed_letters.add(letter)
        print("Correct, trial:", trial)
    else:
        trial -= 1
        print("Don't have letter", letter + ". Trial:", trial)

    if set(name) == guessed_letters:
        print("Done")
        break

if trial == 0:
    print("Die")
