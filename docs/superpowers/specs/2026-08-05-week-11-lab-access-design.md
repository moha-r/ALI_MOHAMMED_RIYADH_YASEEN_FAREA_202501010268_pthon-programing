# Week 11 Computer Lab Access System Design

## Goal

Implement Tutorial 11 exactly as shown in the supplied image: a small modular Python command-line application that decides whether a student may enter the computer lab.

## Required Structure

Create `week_11` with exactly these tutorial files:

- `main.py`
- `student.py`
- `access.py`
- `display.py`
- `README.md`

## Module Responsibilities

### `student.py`

Define `get_student()`. Print the Computer Lab Access heading, prompt for the student's name and ID, then ask whether the student is registered, the lab is open, and a computer is available. Return all five values to the caller.

### `access.py`

Define `check_access(registered, lab_open, computer_available)`. Grant access only when all three answers are `Y`; otherwise deny access.

Define `get_reason(registered, lab_open, computer_available)`. Return the first applicable message in this order:

1. `Student is not registered`
2. `Computer lab is closed`
3. `No available computer`
4. `Welcome to the lab.`

### `display.py`

Define `print_result(name, student_id, status, reason)` and display the student's name, ID, access status, and reason using the layout shown in the expected outcome.

### `main.py`

Import the functions from the other modules, collect the student data, calculate the status and reason, then print the result. Run `main()` only when the file is executed directly.

### `README.md`

Briefly describe the application, required files, and the command `python main.py` used to run it.

## Input and Output Rules

- Preserve the prompt wording and visible headings from the tutorial image.
- Treat uppercase `Y` as yes, matching the tutorial example. Any other response is treated as no.
- Return the exact status strings `Access Granted` and `Access Denied`.
- Keep the implementation short and limited to the tutorial requirements.

## Verification

Run the application with four input sets to verify access granted, student not registered, lab closed, and no computer available. Compile all Python modules to catch syntax errors.
