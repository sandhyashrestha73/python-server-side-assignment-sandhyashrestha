# Step 1: Take student names from user
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# Step 2: Write names into a file
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudent names saved to file successfully!\n")

# Step 3: Read the file
print("Reading from file...\n")

with open("students.txt", "r") as file:
    content = file.read()

# Step 4: Display contents
print("List of Students:")
print(content)