# Student Management CRUD Application

A beginner-friendly **Student Management CRUD Application** built using **Python Flask, MySQL, HTML, CSS, and JavaScript**.

This project demonstrates how a frontend can communicate with a Flask backend and perform complete **CRUD operations** on data stored in a MySQL database.

---

## Project Overview

This application allows users to manage student records through a web interface.

The application supports four main operations:

| Operation | HTTP Method | Description                |
| --------- | ----------- | -------------------------- |
| Create    | POST        | Add a new student          |
| Read      | GET         | Display all students       |
| Update    | PUT         | Update an existing student |
| Delete    | DELETE      | Delete a student           |

The user does not need Postman to use the application. All operations can be performed directly from the HTML webpage.

---

# Application Architecture

The project follows this architecture:

```text
                    WEB BROWSER
                         |
                         |
              HTML + CSS + JavaScript
                         |
                         |
                    Flask API
                         |
                         |
                  MySQL Connector
                         |
                         |
                    MySQL Database
```

The complete flow is:

```text
User
 ↓
HTML Form
 ↓
JavaScript
 ↓
Flask API
 ↓
MySQL Database
 ↓
Flask API
 ↓
JavaScript
 ↓
HTML Page
```

---

# Technologies Used

| Technology             | Purpose                               |
| ---------------------- | ------------------------------------- |
| Python                 | Backend programming                   |
| Flask                  | Web framework and REST API            |
| MySQL                  | Database                              |
| mysql-connector-python | Connect Python with MySQL             |
| HTML                   | Webpage structure                     |
| CSS                    | Webpage styling                       |
| JavaScript             | Frontend interaction and API requests |
| Git                    | Version control                       |
| GitHub                 | Code repository                       |

---

# Project Structure

```text
flask-mysql-crud/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### `app.py`

Contains the Flask application, MySQL connection and CRUD API routes.

### `requirements.txt`

Contains the Python packages required to run the project.

### `templates/index.html`

Contains the frontend HTML page.

### `static/style.css`

Contains the CSS used to style the webpage.

### `README.md`

Contains the project documentation and setup instructions.

---

# Prerequisites

Before starting the project, install the following:

* Python
* MySQL Server
* MySQL Shell or MySQL Command Line Client
* Git
* A web browser

You can optionally install Postman if you want to test the APIs separately.

---

# Step 1 — Clone the Repository

Open Command Prompt or Terminal.

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

For example:

```bash
git clone https://github.com/username/flask-mysql-crud.git
```

Move into the project directory:

```bash
cd flask-mysql-crud
```

---

# Step 2 — Check Python Installation

Run:

```bash
python --version
```

You should see a Python version such as:

```text
Python 3.x.x
```

Also check pip:

```bash
pip --version
```

---

# Step 3 — Create a Virtual Environment

It is recommended to use a virtual environment for this project.

Create the virtual environment:

```bash
python -m venv venv
```

---

# Step 4 — Activate the Virtual Environment

## Windows

For Command Prompt:

```bash
venv\Scripts\activate
```

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

After successful activation, you should see:

```text
(venv)
```

at the beginning of the terminal.

---

# Step 5 — Install Python Dependencies

This project uses a `requirements.txt` file.

Install all required packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
Flask
mysql-connector-python
```

Using `requirements.txt` makes it easy to install all required Python packages with a single command.

---

# Step 6 — Create the MySQL Database

Open MySQL.

You can connect using:

```bash
mysql -u root -p
```

Enter your MySQL password when prompted.

---

# Step 7 — Create the Database

Create a database named:

```text
studentdb
```

Run:

```sql
CREATE DATABASE studentdb;
```

Select the database:

```sql
USE studentdb;
```

---

# Step 8 — Create the Students Table

Create a table named `students`:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

The table contains the following columns:

| Column | Data Type    | Description       |
| ------ | ------------ | ----------------- |
| id     | INT          | Unique student ID |
| name   | VARCHAR(100) | Student name      |
| age    | INT          | Student age       |
| course | VARCHAR(100) | Student course    |

The `id` column automatically increases because it uses:

```sql
AUTO_INCREMENT
```

---

# Step 9 — Add Sample Data

To test the application, add some initial records.

Run:

```sql
INSERT INTO students (name, age, course)
VALUES
('Rahul', 20, 'Python'),
('Priya', 21, 'Java'),
('Amit', 22, 'Data Science');
```

Check the records:

```sql
SELECT * FROM students;
```

You should see something similar to:

```text
+----+-------+-----+-------------+
| id | name  | age | course      |
+----+-------+-----+-------------+
|  1 | Rahul |  20 | Python      |
|  2 | Priya |  21 | Java        |
|  3 | Amit  |  22 | Data Science |
+----+-------+-----+-------------+
```

---

# Step 10 — Configure MySQL in Flask

Open:

```text
app.py
```

Find the MySQL connection:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="studentdb"
)
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your actual MySQL password.

For example:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="studentdb"
)
```

Use the password associated with your MySQL `root` account.

### Important

Do **not** upload your actual MySQL password to GitHub.

For a learning project, the password may be written directly in the code, but for production applications, environment variables should be used.

---

# Step 11 — Run the Flask Application

Make sure the virtual environment is activated.

Run:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

This means the Flask application is running.

---

# Step 12 — Open the Application

Open your web browser and visit:

```text
http://127.0.0.1:5000
```

You should see the Student Management webpage.

The application contains sections for:

* Adding students
* Updating students
* Deleting students
* Viewing all students

---

# CRUD Operations

## 1. GET — Display All Students

When the webpage loads, JavaScript sends a GET request to:

```text
GET /students
```

Flask executes:

```sql
SELECT * FROM students;
```

The data is returned as JSON and displayed in the HTML table.

Example:

```text
ID    Name       Age    Course

1     Rahul      20     Python
2     Priya      21     Java
3     Amit       22     Data Science
```

---

# 2. POST — Add a Student

The **Add Student** section contains:

```text
Name
Age
Course
```

For example:

```text
Name: Akshat
Age: 23
Course: Flask
```

When the user clicks **Add Student**, JavaScript sends:

```text
POST /students
```

with JSON data:

```json
{
    "name": "Akshat",
    "age": 23,
    "course": "Flask"
}
```

Flask receives the data and executes:

```sql
INSERT INTO students
(name, age, course)
VALUES (...);
```

The new student is stored in MySQL.

---

# 3. PUT — Update a Student

The **Update Student** section requires:

```text
Student ID
New Name
New Age
New Course
```

For example:

```text
Student ID: 2
New Name: Priya Sharma
New Age: 22
New Course: Flask
```

JavaScript sends:

```text
PUT /students/2
```

with:

```json
{
    "name": "Priya Sharma",
    "age": 22,
    "course": "Flask"
}
```

Flask executes:

```sql
UPDATE students
SET name = ...,
    age = ...,
    course = ...
WHERE id = 2;
```

The existing student record is updated.

---

# 4. DELETE — Delete a Student

The **Delete Student** section requires:

```text
Student ID
```

For example:

```text
Student ID: 3
```

JavaScript sends:

```text
DELETE /students/3
```

Flask executes:

```sql
DELETE FROM students
WHERE id = 3;
```

The student is removed from the database.

---

# API Endpoints

The Flask application provides these endpoints:

| Method | Endpoint         | Purpose           |
| ------ | ---------------- | ----------------- |
| GET    | `/students`      | Get all students  |
| POST   | `/students`      | Add a new student |
| PUT    | `/students/<id>` | Update a student  |
| DELETE | `/students/<id>` | Delete a student  |

---

# API Flow

## GET

```text
Browser
   ↓
GET /students
   ↓
Flask
   ↓
SELECT * FROM students
   ↓
MySQL
   ↓
JSON Response
   ↓
Browser
```

## POST

```text
HTML Input
   ↓
JavaScript
   ↓
POST /students
   ↓
Flask
   ↓
INSERT INTO students
   ↓
MySQL
```

## PUT

```text
HTML Input
   ↓
JavaScript
   ↓
PUT /students/<id>
   ↓
Flask
   ↓
UPDATE students
   ↓
MySQL
```

## DELETE

```text
HTML Input
   ↓
JavaScript
   ↓
DELETE /students/<id>
   ↓
Flask
   ↓
DELETE FROM students
   ↓
MySQL
```

---

# Understanding the Frontend

The frontend uses JavaScript's `fetch()` function to communicate with Flask.

For example, the GET request:

```javascript
const response = await fetch("/students");
```

The POST request:

```javascript
const response = await fetch("/students", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        age: age,
        course: course
    })
});
```

The PUT request:

```javascript
const response = await fetch(`/students/${id}`, {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        age: age,
        course: course
    })
});
```

The DELETE request:

```javascript
const response = await fetch(`/students/${id}`, {
    method: "DELETE"
});
```

---

# Understanding the Backend

Flask defines different routes for each CRUD operation.

### GET

```python
@app.route("/students", methods=["GET"])
```

### POST

```python
@app.route("/students", methods=["POST"])
```

### PUT

```python
@app.route("/students/<int:id>", methods=["PUT"])
```

### DELETE

```python
@app.route("/students/<int:id>", methods=["DELETE"])
```

Each route communicates with the MySQL database using SQL queries.

---

# Testing the APIs with Postman

Postman is not required to use the application, but it can be used to test the Flask APIs separately.

### Get all students

```text
GET http://127.0.0.1:5000/students
```

### Add student

```text
POST http://127.0.0.1:5000/students
```

Body → raw → JSON:

```json
{
    "name": "John",
    "age": 24,
    "course": "Flask"
}
```

### Update student

```text
PUT http://127.0.0.1:5000/students/1
```

Body:

```json
{
    "name": "John Smith",
    "age": 25,
    "course": "Python"
}
```

### Delete student

```text
DELETE http://127.0.0.1:5000/students/1
```

---

# Troubleshooting

## 1. MySQL Access Denied

If you see:

```text
Access denied for user 'root'@'localhost'
```

Check the MySQL username and password in `app.py`.

Test your MySQL login using:

```bash
mysql -u root -p
```

Make sure the password entered here is the same password configured in Flask.

---

## 2. Database Does Not Exist

If Flask reports that `studentdb` does not exist, create it:

```sql
CREATE DATABASE studentdb;
```

Then:

```sql
USE studentdb;
```

---

## 3. Table Does Not Exist

Create the table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

---

## 4. Flask Is Not Starting

Make sure the virtual environment is activated:

```bash
venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 5. Port 5000 Is Already in Use

Change:

```python
app.run(debug=True)
```

to:

```python
app.run(debug=True, port=5001)
```

Then open:

```text
http://127.0.0.1:5001
```

---

# Learning Outcomes

After completing this project, you will understand:

* How Flask works
* How to create REST API endpoints
* How to connect Flask with MySQL
* How SQL queries work with Flask
* How to use GET, POST, PUT and DELETE
* How HTML forms collect user input
* How JavaScript communicates with Flask
* How JSON is transferred between frontend and backend
* How to display database data on a webpage
* How to build a basic full-stack CRUD application
* How `requirements.txt` is used to manage Python dependencies

---

# Future Improvements

This project can be extended with:

* Student search functionality
* Form validation
* Better error handling
* Login and authentication
* Pagination
* Student profile pages
* Edit buttons directly inside the student table
* Delete buttons for individual rows
* Bootstrap styling
* REST API authentication
* Environment variables for database credentials
* Deployment to a cloud platform

---

# Complete Application Flow

```text
                 STUDENT MANAGEMENT APP

                         USER
                          |
                          ↓
                  HTML + CSS + JS
                          |
          ┌───────────────┼────────────────┐
          ↓               ↓                ↓
         GET             POST             PUT
          |               |                |
          └───────────────┼────────────────┘
                          ↓
                        Flask
                          |
                          ↓
                    MySQL Connector
                          |
                          ↓
                     MySQL Database
                          |
                          ↓
                   students table
                          |
                          ↓
                        Flask
                          |
                          ↓
                  JSON / Response
                          |
                          ↓
                     Web Browser
```

---

# Author

Developed as a beginner-level project to demonstrate **Python Flask + MySQL + HTML + CSS + JavaScript CRUD operations**.
