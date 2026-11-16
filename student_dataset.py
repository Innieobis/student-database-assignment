# CUL-CYB 371
# DATA MINING AND DATA WAREHOUSING
# Assignment Two: Student Dataset

# Import the CSV module
import csv

# Create fictional student records
students = [
    ["24/10001", "Computer Science", 100, 92, 78],
    ["24/10002", "Cyber Security", 100, 85, 71],
    ["24/10003", "Software Engineering", 200, 88, 82],
    ["24/10004", "Computer Science", 200, 76, 65],
    ["24/10005", "Cyber Security", 100, 95, 89],
    ["24/10006", "Software Engineering", 300, 81, 74],
    ["24/10007", "Computer Science", 300, 90, 86],
    ["24/10008", "Software Engineering", 100, 69, 58],
    ["24/10009", "Cyber Security", 200, 87, 77],
    ["24/10010", "Computer Science", 400, 98, 91],
    ["24/10011", "Cyber Security", 200, 73, 62],
    ["24/10012", "Software Engineering", 300, 93, 84],
    ["24/10013", "Cyber Security", 300, 79, 68],
    ["24/10014", "Computer Science", 100, 84, 73],
    ["24/10015", "Cyber Security", 400, 96, 88]
]

# Create a CSV file
with open("student_dataset.csv", "w", newline="") as file:

    # Prepare the CSV writer
    writer = csv.writer(file)

    # Add column headings
    writer.writerow([
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score"
    ])

    # Add all student records
    writer.writerows(students)

# STEP 7: Display success messages
print("Student dataset created successfully!")
print("Total number of students:", len(students))