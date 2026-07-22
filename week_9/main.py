from ticket import create_ticket
from display import display_ticket


def main():

    ticket = create_ticket()

    if ticket["priority"] == "High":
        ticket["technician"] = "John Doe"

    elif ticket["priority"] == "Medium":
        ticket["technician"] = "Jane Smith"

    elif ticket["priority"] == "Low":
        ticket["technician"] = "Bob Johnson"

    display_ticket(ticket)


if __name__ == "__main__":
    main()