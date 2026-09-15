import numpy as np
import pandas as pd
import sqlite3


# Represents a single student, with an in-memory list of grades
class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self._grades = []  # starts empty, since a new student has no grades yet

    # Adds one grade to this student's grade list
    def add_grade(self, grade):
        self._grades.append(grade)

    # Calculates the average of this student's grades, safely handling no grades yet
    def get_average(self):
        if len(self._grades) == 0:
            return 0
        else:
            return sum(self._grades) / len(self._grades)


# Connect to the database (creates the file if it doesn't exist yet)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the students table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
roll_number INTEGER,
avg_grade REAL
)
''')

conn.commit()


# Adds a new student to the database, with no average grade yet
def add_student(name, roll_number):
    cursor.execute(
        "INSERT INTO student (name, roll_number, avg_grade) VALUES (?, ?, ?)",
        (name, roll_number, None)
    )
    conn.commit()


# Updates a student's average grade in the database, found by their roll number
def update_average(roll_number, avg_grade):
    cursor.execute(
        "UPDATE student SET avg_grade = ? WHERE roll_number = ?",
        (avg_grade, roll_number)
    )
    conn.commit()


# --- Demonstration: OOP class usage ---

s1 = student("Ali", 101)
s1.add_grade(85)
s1.add_grade(90)
print(s1.name, "-", s1._grades, "- average:", s1.get_average())


# --- Demonstration: database + pandas analysis ---

# Clear old data so this demo always runs cleanly
cursor.execute("DELETE FROM student")
conn.commit()

add_student("Shahid", 103)
add_student("Mahnoor", 104)
update_average(103, 45)
update_average(104, 50)

# Load all students into a DataFrame for analysis
df = pd.read_sql_query("SELECT * FROM student", conn)
print(df)

# Class average
print("Class average:", df["avg_grade"].mean())

# Top scorer
top = df.loc[df["avg_grade"].idxmax()]
print("Top scorer:", top["name"], top["avg_grade"])

# Pass/fail counts (threshold: 50)
passing = df[df["avg_grade"] >= 50]
failing = df[df["avg_grade"] < 50]
print("Passed:", len(passing))
print("Failed:", len(failing))

# NumPy stats on grades
grades_array = np.array(df["avg_grade"].dropna())
print("Mean (numpy):", grades_array.mean())
print("Std deviation (numpy):", grades_array.std())

# Sort students by grade, highest to lowest, using lambda
students_list = list(zip(df["name"], df["avg_grade"]))
sorted_list = sorted(students_list, key=lambda x: x[1], reverse=True)
print("Sorted by grade:", sorted_list)
