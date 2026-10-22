
students = []



def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
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
add_student()
print("Student added successfully!")
student = {
    "id": "101",
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "phone": "9876543210",
    "email": "rahul@gmail.com"
}


students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
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
    
def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Phone:", student["phone"])
            print("Email:", student["email"])
            return

    print("Student not found.")



add_student()
search_student()
