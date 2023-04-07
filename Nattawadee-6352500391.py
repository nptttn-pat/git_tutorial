import math

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

print("Nattawadee in binary is \n") 
print(toBinary("Nattawadee"))
print("std_id ''6352500391'' in binary is ") 
print(toBinary("6352500391"))
