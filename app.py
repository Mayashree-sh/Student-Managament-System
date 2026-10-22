from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# ---------------- DATABASE ----------------

def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ---------------- LOGIN ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect("/dashboard")

        else:
            return "Invalid Username or Password"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- ADD STUDENT ----------------
@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = request.form["id"]
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        phone = request.form["phone"]
        email = request.form["email"]

        connection = sqlite3.connect("students.db",timeout=10)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (id, name, age, course, phone, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, name, age, course, phone, email))

        connection.commit()
        connection.close()
        

        return "Student added successfully!"

    return render_template("add_student.html")
# ---------------- VIEW STUDENTS ----------------

@app.route("/students")
def view_students():

    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return render_template("students.html", students=students)
# ---------------- SEARCH STUDENT ----------------

@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None

    if request.method == "POST":

        student_id = request.form["id"]

        connection = sqlite3.connect("students.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        connection.close()

    return render_template("search_student.html", student=student)
# ---------------- UPDATE STUDENT ----------------

@app.route("/update", methods=["GET", "POST"])
def update_student():

    if request.method == "POST":

        student_id = request.form["id"]
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        phone = request.form["phone"]
        email = request.form["email"]

        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE students
            SET name=?, age=?, course=?, phone=?, email=?
            WHERE id=?
        """, (name, age, course, phone, email, student_id))

        connection.commit()
        connection.close()

        return "Student updated successfully!"

    return render_template("update_student.html")
# ---------------- DELETE STUDENT ----------------

@app.route("/delete", methods=["GET", "POST"])
def delete_student():

    if request.method == "POST":

        student_id = request.form["id"]

        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        connection.close()

        return "Student deleted successfully!"

    return render_template("delete_student.html")


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    create_database()
    app.run(debug=True)