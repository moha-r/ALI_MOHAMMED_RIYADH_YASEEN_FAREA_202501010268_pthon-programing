# Week 12 Computer Lab Monitoring System Design

## Goal

Complete Tutorial 12 exactly as shown in the supplied assignment image: a small Python command-line program that records and displays the status of five computers and repeats the monitoring cycle until the technician stops it.

## Required Structure

Create `week_12/main.py`. Keep the tutorial solution in this single file, matching the assignment instruction.

## Functions

### `check_computers()`

Create an empty list, use a `for` loop to prompt for the status of computers 1 through 5, convert each response to uppercase, append it to the list, and return the list. The status prompt uses `A/U/M`, where `A` means Available, `U` means Used, and `M` means Maintenance.

### `count_available(computers)`

Start the available count at zero, iterate through the computer statuses, add one for each `A`, and return the final count.

### `display_status(computers, available)`

Print the `LAB STATUS` heading, display computers 1 through 5 with their recorded statuses, print a separator, and show the total number of available computers using the layout from the expected output.

### Monitoring loop

Use a `while` loop to call the three functions for one monitoring cycle. After displaying the results, prompt with `Perform another monitoring cycle? (Y/N): `. Continue only when the uppercase response is `Y`; otherwise end the program.

## Input and Output Rules

- Prompt for exactly five computers per cycle.
- Accept lowercase input by converting status and continuation responses to uppercase.
- Preserve the prompt wording and visible output headings from the assignment image.
- Do not add behavior beyond the tutorial requirements.

## Verification

Do not add automated test files, per the student's request. Compile `main.py` to catch syntax errors and run it with scripted input to confirm one complete cycle and the expected available-computer count.
