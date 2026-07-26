subjects = []
grades = []

# Collecting data
while True:

    user_input_subject = input("Enter subject name (or press enter to end): ")
    if user_input_subject == "":
        print("Ended collecting subject names.")
        break
    else:
        subject = str(user_input_subject.strip())
        subjects.append(subject)
        user_input_grade = input("Enter grade: ")
        grade = int(user_input_grade)
        grades.append(grade)
print(f"Collected {len(subjects)} subjects")

def get_status(grade):
    if grade in (8, 9, 10):
        status = "Excellent"
    elif grade in (6, 7):
        status = "Good"
    elif grade in (4, 5):
        status = "Normal"
    elif grade in (1, 2, 3):
        status = "Bad"
    return status

def calculale_middle_grade(grades):
    total_subjects = len(grades)
    grade_summary = sum(grades)
    middle_grade = grade_summary / total_subjects
    return middle_grade

for N in range(len(subjects)):
    grade = grades[N]
    subject = subjects[N]
    status = get_status(grade)
    print(f"Subject: {subject}, Grade: {grade}, Status: {status}")

avg = calculale_middle_grade(grades)

print(f"Middle grade: {avg}")
