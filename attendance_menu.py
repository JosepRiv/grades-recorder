import attendance

while True:

    print("\n=== Welcome to the Student Attendance Record System! ===".upper())

    print("\n1. Register students\n2. Register attendance\n3. Show registered students\n4. Update student\n5. Delete student\n0. Go Out")

    option = input("\nPlease select an option from the menu to continue: " ).strip()

    if option.isdigit() and int(option) in range(0, 6):

        match int(option):

            case 0:
                print("Leaving...")
                break
            case 1:
                attendance.register_student()
            case 2:
                attendance.register_attendance()
            case 3:
                attendance.show_students()
            case 4:
                attendance.update_student()
            case 5:
                attendance.delete_student()

    else:

        print("Option is not valid.")