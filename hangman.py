letter_of_hangman = str(input("name(only lowletter): "))
check_the_letter = [" "] * len(letter_of_hangman)
number_of_trial = 5

while (number_of_trial != 0 and letter_of_hangman != ""):
  condition = False
  if (''.join(check_the_letter) == letter_of_hangman):
    break
  else:
    guess_letter = input("Guess letter: ")
    for i in range(len(letter_of_hangman)):
      if guess_letter == letter_of_hangman[i]:
         check_the_letter[i] = letter_of_hangman[i]
         condition = True
  if(condition == True ):
      if (''.join(check_the_letter) == letter_of_hangman):
        print("Done")
      else:
        print("Correct, trial: ",number_of_trial)
  else:
    number_of_trial -= 1
    if (number_of_trial == 0):
      print("Die")
    else:
       print("Don’t have letter "+ guess_letter + ". trial: ", number_of_trial)