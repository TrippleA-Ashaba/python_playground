import unittest
from io import StringIO
from unittest.mock import patch
from bagels import get_random_number, validate_input, check_guess


class BagelTestCase(unittest.TestCase):
    def test_get_random_number(self):
        number = get_random_number()
        self.assertGreaterEqual(number, 100)
        self.assertLessEqual(number, 999)

    def test_validate_input_valid(self):
        with patch("builtins.input", return_value="123"):
            user_input = validate_input()
            self.assertEqual(user_input, 123)

    def test_validate_input_invalid(self):
        with patch("builtins.input", side_effect=["abc", "def", "456"]):
            with patch("sys.stdout", new=StringIO()) as output:
                with self.assertRaises(ValueError) as context:
                    validate_input()

                expected_error_message = (
                    "Invalid input. Exceeded maximum number of attempts."
                )
                actual_error_message = str(context.exception).strip()

                self.assertEqual(expected_error_message, actual_error_message)

                self.assertEqual(
                    output.getvalue().strip(),
                    "⚠️⚠️ Invalid input. Enter an Integer ⚠️⚠️",
                )

    def test_check_guess_correct(self):
        result = check_guess(123, 123)
        self.assertEqual(result, "Correct")

    def test_check_guess_fermi(self):
        result = check_guess(123, 153)
        self.assertEqual(result, "FERMI   👌")

    def test_check_guess_pico(self):
        result = check_guess(123, 532)
        self.assertEqual(result, "PICO   🤞")

    def test_check_guess_bagels(self):
        result = check_guess(123, 789)
        self.assertEqual(result, "BAGELS   😖")


if __name__ == "__main__":
    unittest.main()
