students = {}

def add_student():
    # Add a new student record using roll number as the key
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")
    students[roll] = {"name": name, "branch": branch, "marks": marks}
    print("Student added successfully!\n")

def display_students():
    # Display all student records currently stored
    if not students:
        print("No records found.\n")
        return
    print("\n----- All Student Records -----")
    for roll, info in students.items():
        print(f"Roll No: {roll} | Name: {info['name']} | Branch: {info['branch']} | Marks: {info['marks']}")
    print()

def search_student():
    # Search for a student by name
    name = input("Enter name to search: ")
    found = False
    for roll, info in students.items():
        if info["name"].lower() == name.lower():
            print(f"Found -> Roll No: {roll} | Name: {info['name']} | Branch: {info['branch']} | Marks: {info['marks']}")
            found = True
    if not found:
        print("Student not found.\n")
    else:
        print()

def delete_student():
    # Delete a student record using roll number
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student record deleted.\n")
    else:
        print("Roll number not found.\n")

def main():
    while True:
        print("----- Student Record Management System -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
