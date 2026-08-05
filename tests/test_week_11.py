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
