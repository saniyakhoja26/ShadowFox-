"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: File Handling (Student Marks)
"""

import csv

# Dictionary to store student data
students = {}

# 1. Open the CSV file in read mode
with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)

    # 2. Create dictionary from CSV data
    for row in reader:
        name = row["Name"]
        marks = [int(row["Maths"]), int(row["Science"]), int(row["English"])]

        total_marks = sum(marks)
        average_marks = total_marks / len(marks)

        # 3 & 4. Add total_marks and average to dictionary
        students[name] = {
            "Maths": row["Maths"],
            "Science": row["Science"],
            "English": row["English"],
            "Total_Marks": total_marks,
            "Average": average_marks,
        }

print("Student data processed successfully.")

print("\n---------------------------------------\n")

# 5. Create a new CSV file and write updated data
with open("student_marks_updated.csv", "w", newline="") as new_file:
    fieldnames = ["Name", "Maths", "Science", "English", "Total_Marks", "Average"]
    writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    writer.writeheader()

    for name, data in students.items():
        writer.writerow(
            {
                "Name": name,
                "Maths": data["Maths"],
                "Science": data["Science"],
                "English": data["English"],
                "Total_Marks": data["Total_Marks"],
                "Average": round(data["Average"], 2),
            }
        )

print("New CSV file created with total and average marks.")

print("\n---------------------------------------\n")
