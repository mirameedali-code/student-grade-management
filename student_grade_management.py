import sqlite3
import numpy as np
import pandas as pd

class student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade  # Stores the single grade directly

# Database Setup
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_number INTEGER,
    avg_grade REAL
)
''')
conn.commit()

def add_student(name, roll_number, grade):
    cursor.execute("INSERT INTO student (name, roll_number, avg_grade) VALUES (?, ?, ?)", (name, roll_number, grade))
    conn.commit()

def show_analytics():
    df = pd.read_sql_query("SELECT * FROM student", conn)
    if df.empty or df["avg_grade"].isnull().all():
        print("📭 Database is empty or no grades recorded yet.")
        return
        
    print("\n" + "="*10 + " CLASS PERFORMANCE REPORT " + "="*10)
    print("Class average:", df["avg_grade"].mean())
    
    top = df.loc[df["avg_grade"].idxmax()]
    print(f"🏆 Top Scorer: {top['name']} ({top['avg_grade']})")
    
    passing = df[df["avg_grade"] >= 50]
    failing = df[df["avg_grade"] < 50]
    print("✅ Passed:", len(passing))
    print("❌ Failed:", len(failing))
    
    # NumPy calculations on the grades
    grades_array = np.array(df["avg_grade"].dropna())
    print("Mean (numpy):", grades_array.mean())
    print("Std deviation (numpy):", grades_array.std())
    
    # Lambda sorting (highest to lowest)
    students_list = list(zip(df["name"], df["avg_grade"]))
    sorted_list = sorted(students_list, key=lambda x: x[1], reverse=True)
    print("\n📋 Leaderboard:")
    for s in sorted_list:
        print(f" - {s[0]}: {s[1]}")

# --- THE INTERACTIVE MENU LOOP ---
while True:
    print("\n=== STUDENT GRADE SYSTEM ===")
    print("1. Register Student & Grade")
    print("2. View Class Analytics & Leaderboard")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ").strip()
    
    if choice == "1":
        s_name = input("Enter student name: ").strip()
        s_roll = int(input("Enter roll number: "))
        s_grade = float(input("Enter student's grade: ")) # Just asks once!
        
        # Creates the student object using your OOP design
        temp_student = student(s_name, s_roll, s_grade)
        
        # Save directly to database
        add_student(temp_student.name, temp_student.roll_number, temp_student.grade)
        print(f"✅ Saved {temp_student.name} with a grade of {temp_student.grade}")
        
    elif choice == "2":
        show_analytics()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid option.")
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
