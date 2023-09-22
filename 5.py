from itertools import combinations

n_list = [
    int(a) for a in input("Input: ").replace(' ', '').replace('[', '').replace(
        ']', '').split(',')
]
the_list = combinations(n_list, 3)
y = False
for a_list in the_list:
  if sum(a_list) == 0:
    print(f'Output: {[n_list.index(a) for a in a_list]}')
    y = True
if not y:
  print("Output: Can’t find")
