Word = str(input("Name: "))
Check = [" "] * len(Word)
Trial = 5

while (Trial != 0 and Word != ""):
  Found = False
  if (''.join(Check) == Word):
    break
  else:
    Guess_letter = input("Guess letter: ")
    for i in range(len(Word)):
      if Guess_letter == Word[i]:
         Check[i] = Word[i] 
         Found = True  

  if(Found == True ): #check correct
      if (''.join(Check) == Word):
        print("Done")
      else:
        print("Correct, trial: ",Trial) 
  else:
    Trial -= 1
    if (Trial == 0):
      print("Die") #While
    else:
       print("Don’t have letter "+ Guess_letter + ". trial: ", Trial)