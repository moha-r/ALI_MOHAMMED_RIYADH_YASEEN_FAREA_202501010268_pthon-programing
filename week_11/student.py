def get_student():
    print("===== Computer Lab Access =====")

    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Y/N): ")
    lab_open = input("Is the lab open? (Y/N): ")
    computer_available = input("Computer available? (Y/N): ")

    return name, student_id, registered, lab_open, computer_available
