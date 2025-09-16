# Function: Grade calculation
def get_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'd'
    else:
        return 'F'


# Function: Collect student info
def collect_student_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    subjects = input("Enter your subjects (comma or space separated): ")

    # Handle comma / space input
    if "," in subjects:
        subjects_list = [sub.strip() for sub in subjects.split(",")]
    else:
        subjects_list = [sub.strip() for sub in subjects.split()]

    marks_dict = {}
    for subject in subjects_list:
        marks = float(input(f"Enter marks for {subject}: "))
        marks_dict[subject] = marks

    # Total & Average
    total_marks = sum(marks_dict.values())
    average_marks = total_marks / len(marks_dict) if marks_dict else 0
    result = "Pass" if average_marks >= 40 else "Fail"


    # Student record dictionary
    return {
        "name": name,
        "age": age,
        "subjects": subjects_list,
        "marks": marks_dict,
        "total": total_marks,
        "average": average_marks,
        "result": result
    }

# Main Program
students = []
num_students = int(input("Enter number Of students: "))

for i in range(num_students):
    print(f"\n--- Enter details for Student {i+1} ---")
    student_data = collect_student_info()
    students.append(student_data)

# 🎯 Final Report
print("\n===== STUDENT REPORT =====")
for s in students:
    print(f"\nName: {s['name']} | Age: {s['age']}")
    print(f"Subjects: {s['subjects']} | Total: {s['total']} | Average: {s['average']:.2f} | Result: {s['result']}")
    print("--- Subject-wise Marks ---")
    for subject, marks in s['marks'].items():
        grade = get_grade(marks)
        print(f"{subject}: {marks} → Grade: {grade}")