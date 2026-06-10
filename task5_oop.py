class Student:
    # Constructor to initialize attributes
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0

    # Method to take input
    def input_details(self):
        self.name = input("Enter student name: ")
        self.roll_number = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    # Method to display details
    def display_details(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


# Create object of Student class
student1 = Student()

# Input details
student1.input_details()

# Display details
student1.display_details()