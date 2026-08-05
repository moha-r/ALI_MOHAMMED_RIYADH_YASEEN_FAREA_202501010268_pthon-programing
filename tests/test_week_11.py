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


if __name__ == "__main__":
    unittest.main()
