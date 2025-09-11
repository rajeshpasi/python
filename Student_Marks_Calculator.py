
name = input("Enter your name:")
age = int(input("Enter your age:"))
subjects = input("Enter your subjects (comma separated):")
if "," in subjects: # Check if input contains commas
    subjects_list = [sub.strip() for sub in subjects.split(',')] # Splitting and stripping whitespace from subjects
else:
    subjects_list = [sub.strip() for sub in subjects.split()] # Splitting and stripping whitespace from subjects

# Dictionary to store marks
marks_dict = {}

# Input marks for each subject
for subject in subjects_list:
    marks = float(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks

# Calculations
total_marks = sum(marks_dict.values())
average_marks = total_marks / len(marks_dict) if marks_dict else 0
result = "Pass" if average_marks >= 40 else "Fail"


# Output
print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("Subjects:", subjects_list)
print("Number of subjects:", len(subjects_list))
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Result:", result)

print("\n--- Marks Subject-wise with Grade ---")
for subject, marks in marks_dict.items():
    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B+'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'F'

    # अब यहीं print करो
    print(f"{subject}: {marks} → Grade: {grade}")