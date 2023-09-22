n = int(input("Enter an integer: "))

a = 0
b = 1
temp = 0
for i in range(n):
  if i == 0:
    print(1)
  else:
    temp = a + b
    print(temp)
    a = b
    b = temp
