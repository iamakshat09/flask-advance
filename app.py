from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)


# MySQL Connection
def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="studentdb"
    )

    return connection


# --------------------------------
# HOME PAGE
# --------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# --------------------------------
# GET - Get all students
# --------------------------------

@app.route("/students", methods=["GET"])
def get_students():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(students)


# --------------------------------
# POST - Add new student
# --------------------------------

@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    name = data["name"]
    age = data["age"]
    course = data["course"]

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO students (name, age, course)
        VALUES (%s, %s, %s)
    """

    values = (name, age, course)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student added successfully"
    })


# --------------------------------
# PUT - Update student
# --------------------------------

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.json

    name = data["name"]
    age = data["age"]
    course = data["course"]

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
        UPDATE students
        SET name = %s,
            age = %s,
            course = %s
        WHERE id = %s
    """

    values = (name, age, course, id)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student updated successfully"
    })


# --------------------------------
# DELETE - Delete student
# --------------------------------

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (id,))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Student deleted successfully"
    })


# --------------------------------
# RUN APPLICATION
# --------------------------------

if __name__ == "__main__":

    app.run(debug=True)