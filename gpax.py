def calculate_gpa(raw_scores):
    gpa_scale = {
        'A': 4.0,
        'A-': 3.5,
        'B+': 3.0,
        'B': 2.5,
        'B-': 2.0,
        'C+': 1.5,
        'C': 1.0,
        'F': 0.0
    }

    total_points = 0
    total_credits = len(raw_scores)

    for raw_score in raw_scores:
        if raw_score >= 80:
            grade = 'A'
        elif raw_score >= 75:
            grade = 'A-'
        elif raw_score >= 70:
            grade = 'B+'
        elif raw_score >= 65:
            grade = 'B'
        elif raw_score >= 60:
            grade = 'B-'
        elif raw_score >= 55:
            grade = 'C+'
        elif raw_score >= 50:
            grade = 'C'
        else:
            grade = 'F'

        total_points += gpa_scale[grade]

    if total_credits == 0:
        return 0.0  # Avoid division by zero

    return total_points / total_credits

try:
    raw_scores_str = input("Input: ")
    raw_scores = [int(score) for score in raw_scores_str.strip('[]').split(',')]

    gpa = calculate_gpa(raw_scores)
    print(f"{gpa:.3f}")

except ValueError:
    print("Invalid input. Please enter raw scores as integers separated by commas inside square brackets.")
