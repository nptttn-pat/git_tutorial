name = 'nutchanon'
name = list(name)
trial = 5
while True:
  x = input('Guess letter: ')
  if x in name:
    print(f'Correct, trial: {trial}')
    
    for i, letter in enumerate(name):
      if x == letter:
        name.pop(i)
        
    if len(name) == 0:
      print('Done')
      break
  else:
    trial -= 1
    if trial == 0:
      print('Die')
      break
    else:
      print(f'Don’t have letter {x}. trial: {trial}')
