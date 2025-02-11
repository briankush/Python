def determine_grade(scores):
    if 90 <= scores <= 100:
        return 'A'
    elif 80 <= scores < 90:
        return 'B'
    elif 70 <= scores < 80:
        return 'C'
    elif 60 <= scores < 70:
        return 'D'
    else:
        return 'F'

# Get user input for the student's score
try:
    student_score = float(input("Enter the student's score: "))
    if 0 <= student_score <= 100:
        grade = determine_grade(student_score)
        print(f"Student score: {student_score}, Grade: {grade}")
    else:
        print("Invalid input! Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a valid numeric score.")
