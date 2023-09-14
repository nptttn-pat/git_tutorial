def Score_Grade(Score):
    if (Score >= 80):
        Grade = 4.0
    elif (Score >= 75 and Score <= 79):
        Grade = 3.5
    elif (Score >= 70 and Score <= 74):
        Grade = 3.0
    elif (Score >= 65 and Score <= 69):
        Grade = 2.5
    elif (Score >= 60 and Score <= 64):
        Grade = 2.0
    elif (Score >= 55 and Score <= 59):
        Grade = 1.5
    elif (Score >= 50 and Score <= 54):
        Grade = 1.0
    else:
        Grade = 0.0

    return Grade

def AvgCal():
    Total = 0
    for i in range(len(Input)):
        Total += Grades[i]
    Output = Total / len(Input)
    return Output

#Main

Input = [80, 65, 55, 79]
Grades = [" "] * len(Input)

for i in range(len(Input)):
    Grades[i] = Score_Grade(Input[i])

Output = AvgCal()
print("Output:", Output)
