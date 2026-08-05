def check_access(registered, lab_open, computer_available):
    if registered == "Y" and lab_open == "Y" and computer_available == "Y":
        return "Access Granted"

    return "Access Denied"


def get_reason(registered, lab_open, computer_available):
    if registered != "Y":
        return "Student is not registered"
    if lab_open != "Y":
        return "Computer lab is closed"
    if computer_available != "Y":
        return "No available computer"

    return "Welcome to the lab."
