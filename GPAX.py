def grading(score):
    if (score >= 80):
        Grade = 4.0
    elif (score >= 75 and score <= 79):
        Grade = 3.5
    elif (score >= 70 and score <= 74):
        Grade = 3.0
    elif (score >= 65 and score <= 69):
        Grade = 2.5
    elif (score >= 60 and score <= 64):
        Grade = 2.0
    elif (score >= 55 and score <= 59):
        Grade = 1.5
    elif (score >= 50 and score <= 54):
        Grade = 1.0
    else:
        Grade = 0.0
    return Grade

def cal():
    total = 0
    for i in range(len(Input)):
        total += Grades[i]
    Output = total / len(Input)
    return Output

Input = [80, 65, 55, 79]
Grades = [" "] * len(Input)

for i in range(len(Input)):
    Grades[i] = grading(Input[i])

Output = cal()
print("Output:", Output)
