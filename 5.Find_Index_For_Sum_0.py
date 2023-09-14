Input = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
print("Input:",Input)
#Input = [1,2,3,4,5]
Find = False

for i in range(0,len(Input)-2):
    for j in range(i+1,len(Input)-1):
        for k in range(j+1,len(Input)):
            if (Input[i]+Input[j]+Input[k] == 0):
                Find = True
                
if (Find):
    print('Output:',[i,j,k])
else:
    print("Can’t find")
