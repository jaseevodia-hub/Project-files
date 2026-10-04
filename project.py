students = {}

while True:
    print("\n=== Student Grade Manager ===")
    print("1. Add student")
    print("2. Remove student")
    print("3. View students")
    print("4. Search student")
    print("5. Add grade")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            student_id = input("Student ID: ")
            if not student_id.isdigit():
                print("This must contain only digits.")

            if student_id in students:
                print("Student already exists.")
                continue

            name = input("Student name: ")
            if not name.isalpha():
                print("Student name must contain only letters.")

            course = input("Student course: ")
            if not course.isalpha():
                print("Student course must also contain letters.")

            students[student_id] = {
                "name": name,
                "course": course,
                "grades": []
            }
            print("Student added successfully!")

        elif choice == "2":
            student_id = input("Student ID to remove: ")

            if student_id in students:
                del students[student_id]
                print("Student removed successfully!")
            else:
                print("Student not found.")

        elif choice == "3":
            if not students:
                print("No students available.")
            else:
                for sid, s in students.items():
                    print(f"\nID: {sid}")
                    print(f"Name: {s['name']}")
                    print(f"Course: {s['course']}")
                    print(f"Grades: {s['grades']}")

        elif choice == "4":
            student_id = input("Student ID to search: ")

            if student_id in students:
                s = students[student_id]
                print(f"Name: {s['name']}")
                print(f"Course: {s['course']}")
                print(f"Grades: {s['grades']}")
            else:
                print("Student not found.")

        elif choice == "5":
            student_id = input("Student ID: ")

            if student_id not in students:
                print("Student not found.")
                continue

            grade = input("Enter grade: ")

            grade = input("Enter grade: ")

            if grade.isdigit() and 0 <= int(grade) <= 100:
                students[student_id]["grades"].append(int(grade))
                print("Grade added successfully!")
            else:
                raise ValueError("Grade must be an integer between 0 and 100.")


        elif choice == "6":
            print("Thank you for using this program ❤")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid number.")