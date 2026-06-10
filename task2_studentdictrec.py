students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        roll = input("Enter roll number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            contact = input("Enter contact number: ")

            students[roll] = {
                "name": name,
                "marks": marks,
                "contact": contact
            }

            print("Student added successfully!")

    # Search student
    elif choice == "2":
        roll = input("Enter roll number to search: ")

        if roll in students:
            print("\nStudent Found:")
            print("Roll:", roll)
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
            print("Contact:", students[roll]["contact"])
        else:
            print("Student not found!")

    # Display all students
    elif choice == "3":
        if not students:
            print("No student records found!")
        else:
            print("\nAll Student Records:")
            for roll, info in students.items():
                print("\nRoll:", roll)
                print("Name:", info["name"])
                print("Marks:", info["marks"])
                print("Contact:", info["contact"])

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")