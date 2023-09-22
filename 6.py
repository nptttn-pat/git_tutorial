def raw_to_grade(n):
  if n >= 80:
    return 4.0
  elif n >= 75:
    return 3.5
  elif n >= 70:
    return 3.0
  elif n >= 65:
    return 2.5
  elif n >= 60:
    return 2.0
  elif n >= 55:
    return 1.5
  elif n >= 50:
    return 1.0
  else:
    return 0

raw_list = input("Input: ")
raw_list = raw_list.strip("[]").split(",")
raw_list = [int(x) for x in raw_list]
grade_list = [raw_to_grade(n) for n in raw_list]
gpax = sum(grade_list) / len(grade_list)
print(f'Output: {gpax}')
