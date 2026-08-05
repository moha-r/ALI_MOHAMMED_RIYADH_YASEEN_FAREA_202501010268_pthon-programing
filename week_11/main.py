from access import check_access, get_reason
from display import print_result
from student import get_student


def main():
    name, student_id, registered, lab_open, computer_available = get_student()

    status = check_access(registered, lab_open, computer_available)
    reason = get_reason(registered, lab_open, computer_available)

    print_result(name, student_id, status, reason)


if __name__ == "__main__":
    main()
