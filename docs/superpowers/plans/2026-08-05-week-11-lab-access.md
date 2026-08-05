# Week 11 Computer Lab Access System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Week 11 modular Python command-line application exactly as specified in the tutorial image.

**Architecture:** `student.py` collects five input values, `access.py` converts the three access conditions into a status and reason, `display.py` renders the result, and `main.py` coordinates the modules. Standard-library `unittest` tests exercise every access outcome and the module integration without adding runtime dependencies.

**Tech Stack:** Python 3.9, Python standard library, `unittest`, Markdown

---

## File Structure

- Create `week_11/student.py`: collect student and lab input.
- Create `week_11/access.py`: decide status and reason.
- Create `week_11/display.py`: print the access result.
- Create `week_11/main.py`: coordinate the application.
- Create `week_11/README.md`: explain purpose, modules, and execution.
- Create `tests/test_week_11.py`: verify the tutorial behavior without changing the required `week_11` file list.

### Task 1: Access decision logic

**Files:**
- Create: `tests/test_week_11.py`
- Create: `week_11/access.py`

- [ ] **Step 1: Write the failing access tests**

```python
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK_11 = ROOT / "week_11"


def load_week_11_module(test_case, module_name):
    module_path = WEEK_11 / f"{module_name}.py"
    if not module_path.exists():
        test_case.fail(f"Missing tutorial module: {module_path}")

    spec = importlib.util.spec_from_file_location(
        f"week_11_{module_name}", module_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AccessTests(unittest.TestCase):
    def setUp(self):
        self.access = load_week_11_module(self, "access")

    def test_grants_access_when_all_conditions_are_yes(self):
        self.assertEqual(
            self.access.check_access("Y", "Y", "Y"), "Access Granted"
        )
        self.assertEqual(
            self.access.get_reason("Y", "Y", "Y"), "Welcome to the lab."
        )

    def test_denies_access_when_student_is_not_registered(self):
        self.assertEqual(
            self.access.check_access("N", "Y", "Y"), "Access Denied"
        )
        self.assertEqual(
            self.access.get_reason("N", "Y", "Y"),
            "Student is not registered",
        )

    def test_denies_access_when_lab_is_closed(self):
        self.assertEqual(
            self.access.check_access("Y", "N", "Y"), "Access Denied"
        )
        self.assertEqual(
            self.access.get_reason("Y", "N", "Y"),
            "Computer lab is closed",
        )

    def test_denies_access_when_no_computer_is_available(self):
        self.assertEqual(
            self.access.check_access("Y", "Y", "N"), "Access Denied"
        )
        self.assertEqual(
            self.access.get_reason("Y", "Y", "N"),
            "No available computer",
        )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the access tests and verify the expected failure**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: four failures reporting `Missing tutorial module: .../week_11/access.py`.

- [ ] **Step 3: Implement the access functions**

```python
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
```

- [ ] **Step 4: Run the access tests and verify they pass**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: `Ran 4 tests` and `OK`.

- [ ] **Step 5: Commit the access logic**

```bash
git add tests/test_week_11.py week_11/access.py
git commit -m "feat: add week 11 access decisions"
```

### Task 2: Result display

**Files:**
- Modify: `tests/test_week_11.py`
- Create: `week_11/display.py`

- [ ] **Step 1: Add the failing display test before the final `if __name__` block**

```python
class DisplayTests(unittest.TestCase):
    def test_prints_access_result_in_tutorial_layout(self):
        import contextlib
        import io

        display = load_week_11_module(self, "display")
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            display.print_result(
                "izzad", "202505", "Access Granted", "Welcome to the lab."
            )

        self.assertEqual(
            output.getvalue(),
            "\n========== ACCESS RESULT ==========\n"
            "Student Name : izzad\n"
            "Student ID   : 202505\n"
            "-----------------------------------\n"
            "Status : Access Granted\n"
            "Reason : Welcome to the lab.\n"
            "===================================\n",
        )
```

- [ ] **Step 2: Run the display test and verify the expected failure**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: failure reporting `Missing tutorial module: .../week_11/display.py`.

- [ ] **Step 3: Implement the result display**

```python
def print_result(name, student_id, status, reason):
    print("\n========== ACCESS RESULT ==========")
    print(f"Student Name : {name}")
    print(f"Student ID   : {student_id}")
    print("-----------------------------------")
    print(f"Status : {status}")
    print(f"Reason : {reason}")
    print("===================================")
```

- [ ] **Step 4: Run all current tests**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: `Ran 5 tests` and `OK`.

- [ ] **Step 5: Commit the result display**

```bash
git add tests/test_week_11.py week_11/display.py
git commit -m "feat: display week 11 access result"
```

### Task 3: Student input collection

**Files:**
- Modify: `tests/test_week_11.py`
- Create: `week_11/student.py`

- [ ] **Step 1: Add the failing student-input test before the final `if __name__` block**

```python
class StudentTests(unittest.TestCase):
    def test_collects_the_five_tutorial_values(self):
        from unittest.mock import patch

        student = load_week_11_module(self, "student")

        with patch(
            "builtins.input",
            side_effect=["izzad", "202505", "Y", "Y", "Y"],
        ) as mocked_input:
            result = student.get_student()

        self.assertEqual(result, ("izzad", "202505", "Y", "Y", "Y"))
        self.assertEqual(
            [call.args[0] for call in mocked_input.call_args_list],
            [
                "Student Name : ",
                "Student ID : ",
                "Registered for today's lab? (Y/N): ",
                "Is the lab open? (Y/N): ",
                "Computer available? (Y/N): ",
            ],
        )
```

- [ ] **Step 2: Run the student test and verify the expected failure**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: failure reporting `Missing tutorial module: .../week_11/student.py`.

- [ ] **Step 3: Implement student input collection**

```python
def get_student():
    print("===== Computer Lab Access =====")

    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Y/N): ")
    lab_open = input("Is the lab open? (Y/N): ")
    computer_available = input("Computer available? (Y/N): ")

    return name, student_id, registered, lab_open, computer_available
```

- [ ] **Step 4: Run all current tests**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: `Ran 6 tests` and `OK`.

- [ ] **Step 5: Commit student input collection**

```bash
git add tests/test_week_11.py week_11/student.py
git commit -m "feat: collect week 11 student details"
```

### Task 4: Application integration

**Files:**
- Modify: `tests/test_week_11.py`
- Create: `week_11/main.py`

- [ ] **Step 1: Add the failing integration test before the final `if __name__` block**

```python
class MainTests(unittest.TestCase):
    def test_connects_input_access_and_display_modules(self):
        import sys
        from unittest.mock import patch

        sys.path.insert(0, str(WEEK_11))
        try:
            main = load_week_11_module(self, "main")
        finally:
            sys.path.pop(0)

        with patch.object(
            main,
            "get_student",
            return_value=("izzad", "202505", "Y", "Y", "Y"),
        ), patch.object(main, "print_result") as mocked_print:
            main.main()

        mocked_print.assert_called_once_with(
            "izzad", "202505", "Access Granted", "Welcome to the lab."
        )
```

- [ ] **Step 2: Run the integration test and verify the expected failure**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: failure reporting `Missing tutorial module: .../week_11/main.py`.

- [ ] **Step 3: Implement the application coordinator**

```python
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
```

- [ ] **Step 4: Run the complete automated test suite**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: `Ran 7 tests` and `OK`.

- [ ] **Step 5: Commit the integrated application**

```bash
git add tests/test_week_11.py week_11/main.py
git commit -m "feat: integrate week 11 lab access app"
```

### Task 5: Tutorial README and final verification

**Files:**
- Create: `week_11/README.md`

- [ ] **Step 1: Write the tutorial README**

````markdown
# Computer Lab Access System

## Purpose

This modular Python application checks whether a student may enter the City University computer lab.

A student receives access only when:

- The student is registered for today's lab.
- The computer lab is open.
- A computer is available.

## Files

- `main.py` integrates and runs the application.
- `student.py` collects the student and lab details.
- `access.py` determines the access status and reason.
- `display.py` prints the access result.

## How to Run

Open a terminal in the `week_11` directory and run:

```bash
python3 main.py
```

Answer each prompt using `Y` for yes or `N` for no.
````

- [ ] **Step 2: Compile every Week 11 Python module**

Run: `python3 -m py_compile week_11/main.py week_11/student.py week_11/access.py week_11/display.py`

Expected: exit code 0 with no output.

- [ ] **Step 3: Run the full automated tests**

Run: `python3 -m unittest discover -s tests -p 'test_week_11.py' -v`

Expected: `Ran 7 tests` and `OK`.

- [ ] **Step 4: Run the granted-access example from the tutorial**

Run: `printf 'izzad\n202505\nY\nY\nY\n' | python3 week_11/main.py`

Expected output includes `Status : Access Granted` and `Reason : Welcome to the lab.`.

- [ ] **Step 5: Run the three denial examples**

Run:

```bash
printf 'Ali\n202501\nN\nY\nY\n' | python3 week_11/main.py
printf 'Ali\n202501\nY\nN\nY\n' | python3 week_11/main.py
printf 'Ali\n202501\nY\nY\nN\n' | python3 week_11/main.py
```

Expected reasons, in order: `Student is not registered`, `Computer lab is closed`, and `No available computer`.

- [ ] **Step 6: Check the diff and required file list**

Run:

```bash
git diff --check
find week_11 -maxdepth 1 -type f -print | sort
```

Expected: no whitespace errors and exactly the five tutorial files.

- [ ] **Step 7: Commit the README**

```bash
git add week_11/README.md
git commit -m "docs: explain week 11 lab access app"
```

- [ ] **Step 8: Push the completed main branch**

Run: `git push origin main`

Expected: the local `main` commit range is uploaded to `origin/main`.
