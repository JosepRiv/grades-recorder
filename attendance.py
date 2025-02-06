# attendance.py
import random

courses = {"Investigación de Mercados": {},"Programación Orientada a Objetos": {},"Base de Datos": {},"Arquitectura de Computadoras": {},"Informática Aplicada en TI": {},"Comprensión y Producción de Textos": {},"Aplicación del Calculo y Estadística": {}}

students = {}


def generate_unique_code():
    """Generate a unique student code that doesn't exist in the students dictionary"""
    while True:
        code = str(random.randint(100000, 999999))
        if code not in students:
            return code


def validate_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt).strip()
        if validation_func(value):
            return value
        print(error_message)


def is_valid_name(name):
    return name.replace(" ", "").isalpha()


def register_student():
    number_of_students = validate_input(
        "\nEnter the number of students to register: ",
        lambda x: x.isdigit(),
        "\nNumber is not valid."
    )

    for _ in range(int(number_of_students)):
        student_name = validate_input(
            "\nEnter the student's full name: ",
            is_valid_name,
            "\nThe characters are not valid"
        ).lower()

        student_last_name = validate_input(
            "Enter the student's full last name: ",
            is_valid_name,
            "\nThe characters are not valid"
        ).lower()

        student_code = generate_unique_code()
        students[student_code] = f"{student_last_name} {student_name}"

        # Initialize attendance records for all courses
        for course in courses:
            courses[course][student_code] = []

        print(
            f"\nStudent {student_last_name.title()}, {student_name.title()} has been registered.\nStudent code: {student_code}")

    print("\nSTUDENTS SUCCESSFULLY REGISTERED!!!")


def register_single_attendance(course_name, student_code):
    """Register attendance for a single student in a specific course"""
    if len(courses[course_name][student_code]) == 16:
        print("Student attendance has already been recorded.")
        return

    print(f"\n=== {students[student_code].upper()} ===\n")

    for week in range(16):
        print(f"Week {week + 1}:")
        attendance_status = validate_input(
            "Enter the student's attendance ('A' : Attended, 'T' : Tardy, 'F' : Absent): ",
            lambda x: x.upper() in ['A', 'T', 'F'],
            "Option not valid. Try again."
        ).upper()
        courses[course_name][student_code].append(attendance_status)

    print("\nATTENDANCE REGISTERED SUCCESSFULLY!!")


def register_attendance():
    if not students:
        print("\nTHERE ARE NO STUDENTS REGISTERED!!")
        return

    while True:
        print(f"\n========== CURRENT COURSES ==========\n")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")
        print("0. Go Out")

        course_num = validate_input(
            "\nEnter the course number to record attendance: ",
            lambda x: x.isdigit() and 0 <= int(x) <= len(courses),
            "\nNumber is not valid."
        )

        if course_num == "0":
            print("Leaving...")
            break

        course_name = list(courses.keys())[int(course_num) - 1]

        while True:
            print(f"\n===== STUDENTS ENROLLED IN THE COURSE: {course_name} =====\n")

            for key in courses[course_name]:
                print(f"-> Student: {students[key].title()} - Student code: {key}")

            student_code = input("\nEnter the student code to register their attendance: '0: Go out': ").strip()

            if student_code == "0":
                print("Leaving...")
                break

            if student_code in courses[course_name]:
                register_single_attendance(course_name, student_code)
            else:
                print("The student code is not valid or has not been found!!")


def calculate_attendance_stats(attendance_list):
    if not attendance_list:
        return 0, 0, "No attendance recorded"

    absences = attendance_list.count('F')
    percentage = (absences / len(attendance_list)) * 100
    status = 'Not failed due to non-attendance' if percentage < 30 else 'Failed due to non-attendance'

    return absences, percentage, status


def show_students():
    if not students:
        print("\nTHERE ARE NO STUDENTS REGISTERED!!")
        return

    while True:
        print("\n=== STUDENT DETAILS ===\n")
        for key, value in students.items():
            print(f"-> Student: {value.title()} - Student code: {key}")

        student_code = input("\nEnter the student code ('0: Go out'): ").strip()

        if student_code == "0":
            print("Leaving...")
            break

        if student_code in students:
            print(f"\n===== {students[student_code].upper()} =====")
            print(f"Student code: {student_code}")
            print("Career: Diseño y Desarrollo de Software")
            print("Cycle: 2")

            for course, attendance in courses.items():
                if student_code in attendance:
                    print(f"\n-> Course: {course} - Attendance: {attendance[student_code]}")

                    if attendance[student_code]:
                        absences, percentage, status = calculate_attendance_stats(attendance[student_code])
                        print(
                            f"  Number of absences: {absences} - Percentage of absences: {percentage}% - Status: {status}")
        else:
            print("The student code is not valid or has not been found!!")


def update_student():
    if not students:
        print("\nTHERE ARE NO STUDENTS REGISTERED!!")
        return

    while True:
        for key, value in students.items():
            print(f"\n-> Student: {value.title()} - Student code: {key}")

        student_code = input("\nEnter the student code to update their data ('0': Go Out): ").strip()

        if student_code == "0":
            print("Leaving...")
            break

        if student_code in students:
            new_name = validate_input(
                "\nEnter the new student names: ",
                is_valid_name,
                "The characters are not valid"
            ).lower()

            new_last_name = validate_input(
                "Enter the new student last names: ",
                is_valid_name,
                "The characters are not valid"
            ).lower()

            students[student_code] = f"{new_last_name} {new_name}"
            print("\nSTUDENT UPDATED SUCCESSFULLY!!")
            break
        else:
            print("The student code is not valid or has not been found!!")


def delete_student():
    if not students:
        print("\nTHERE ARE NO STUDENTS REGISTERED!!")
        return

    while True:
        for key, value in students.items():
            print(f"\n-> Student: {value.title()} - Student code: {key}")

        student_code = input("\nEnter the student code to delete their data ('0': Go Out): ").strip()

        if student_code == "0":
            print("Leaving...")
            break

        if student_code in students:
            # Remove student from all courses
            for course in courses.values():
                course.pop(student_code, None)

            # Remove student from students dictionary
            students.pop(student_code)
            print("\nSTUDENT SUCCESSFULLY DELETED!!")
            break
        else:
            print("The student code is not valid or has not been found!!")