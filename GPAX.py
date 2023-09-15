def grade(n):
    if n >= 80:
        grade = 4.0
    elif 75 <= n <= 79:
        grade = 3.5
    elif 70 <= n <= 74:
        grade = 3.0
    elif 65 <= n <= 69:
        grade = 2.5
    elif 60 <= n <= 64:
        grade =2.0
    elif 55 <= n <= 59:
        grade = 1.5
    elif 50 <= n <= 54:
        grade = 1.0
    else:
        grade = 0.0
    
    return grade


def cal(Input):
    sum = 0
    for i in range(len(Input)):
        output = grade(Input[i])
        sum += output
    GPAX = sum/len(Input)
    return GPAX
    

Input = [80, 65, 55, 79]
GPAX = cal(Input)
print("Input:",Input)
print("Output:", GPAX)
