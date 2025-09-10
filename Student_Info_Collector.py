#Enter your name: Rajesh
#Enter your age: 18
#Enter your subjects (comma separated): Math, Physics, CS

name = input("Enter your name:")
age = int(input("Enter your age:"))
subjects = input("Enter your subjects (comma separated):")
if "," in subjects: # Check if input contains commas
    subjects_list = [sub.strip() for sub in subjects.split(',')] # Splitting and stripping whitespace from subjects
else:
    subjects_list = [sub.strip() for sub in subjects.split()] # Splitting and stripping whitespace from subjects

print("Name:", name)
print("Age:", age)
print("Subjects:", subjects_list)
print("Number of subjects:",len(subjects_list))