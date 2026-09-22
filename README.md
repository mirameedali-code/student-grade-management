# Student Grade Management System

A Python + SQLite application for managing students and their grades, with statistical analysis using pandas and numpy.

## Features
- Add students to a database
- Update a student's average grade
- Calculate class average, top scorer, and pass/fail counts
- Analyze grade distribution using numpy (mean, standard deviation)
- Sort students by grade using lambda functions

## Technologies Used
- Python (OOP)
- SQLite (via `sqlite3`)
- pandas
- numpy

## How to Run
1. Open the notebook in Google Colab or any Python environment
2. Run all cells
3. The demonstration section shows adding students, updating grades, and viewing full statistics

## 📈 Example Output & Statistical Analytics

Running the application calculates classroom statistics using NumPy and pandas, generating the following dashboard layout:

```text
======================================
     CLASS PERFORMANCE REPORT         
======================================
 🏆 Top Scorer:    Mahnoor (50.00)
 📊 Class Average: 47.50
--------------------------------------
 STATUS BREAKDOWN:
  ✅ Passed:       1 student(s)
  ❌ Failed:       1 student(s)
======================================
```
