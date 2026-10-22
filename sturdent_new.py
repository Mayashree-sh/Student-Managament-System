students = []


# ---------------- ADD STUDENT ----------------
def add_student():
    print("\n----- Add Student -----")

    student_id = int(input("Enter Student ID: "))

    # Check whether ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "phone": phone,
        "email": email
    }

    students.append(student)

    print("Student added successfully!")


# ---------------- VIEW STUDENTS ----------------
def view_students():
    print("\n----- Student Records -----")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("----------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Phone:", student["phone"])
        print("Email:", student["email"])


# ---------------- SEARCH STUDENT ----------------
def search_student():
    print("\n----- Search Student -----")

    student_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("----------------------------")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Phone:", student["phone"])
            print("Email:", student["email"])
            return

    print("Student not found.")


# ---------------- UPDATE STUDENT ----------------
def update_student():
    print("\n----- Update Student -----")

    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == student_id:

            print("Student found.")

            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")
            student["phone"] = input("Enter new phone number: ")
            student["email"] = input("Enter new email: ")

            print("Student updated successfully!")
            return

    print("Student not found.")


# ---------------- DELETE STUDENT ----------------
def delete_student():
    print("\n----- Delete Student -----")

    student_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# ---------------- MAIN MENU ----------------
def main():
    while True:

        print("\n====================================")
        print(" Student Record Management System")
        print("====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()