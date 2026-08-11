def get_data (subjects, grades):
    while True:
        input_subject = input("Enter subject name (or press enter to end): ")
        if input_subject == "": 
            print("Ended collecting subject names.")
            break
        else:
            subject = input_subject.strip()
            grade = int(input("Enter grade: "))
            subjects.append(subject)
            grades.append(grade)
    return subjects, grades

def get_status(grade):
    if grade in (8, 9, 10):
        status = "Excellent"
    elif grade in (6, 7):
        status = "Good"
    elif grade in (4, 5):
        status = "Normal"
    elif grade in (1, 2, 3):
        status = "Bad"
    else:
        status = "Unknown"
    return status

def calculate_middle_grade(grades):
    total_subjects = len(grades)
    grade_summary = sum(grades)
    middle_grade = grade_summary / total_subjects
    return middle_grade

def print_summary(subjects, grades, avg):
    for N, (subject, grade) in enumerate(zip(subjects, grades)):
        status = get_status(grade)
        print(f"{N+1}. {subject}: {grade}, ({status})")
    print(f"Middle grade: {avg}")


def main():
    subjects = [] 
    grades = []
    get_data(subjects, grades)
    avg = calculate_middle_grade(grades)
    print_summary(subjects, grades, avg)

main()