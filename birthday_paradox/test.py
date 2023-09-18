import calendar
import unittest

from birthday_paradox import (
    find_first_duplicate,
    generate_birthdays,
    get_random_birthday,
)


class TestGetRandomBirthday(unittest.TestCase):
    def test_get_random_birthday(self):
        YEAR = 2023

        birthday = get_random_birthday()

        # Check if the returned birthday is a string
        self.assertIsInstance(birthday, str)

        # Check if the birthday has the correct format
        self.assertRegex(birthday, r"^[A-Za-z]{3} \d{1,2}$")

        # Split the birthday into month and day
        month, day = birthday.split(" ")

        # Define a list of month abbreviations
        month_abbr = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]

        # Check if the month is a valid month abbreviation
        self.assertIn(month, month_abbr)

        # Check if the day is within the valid range for the month
        month_num = (
            month_abbr.index(month) + 1
        )  # Add 1 to match calendar month numbering
        days_in_month = calendar.monthrange(year=YEAR, month=month_num)[1]
        self.assertTrue(1 <= int(day) <= days_in_month)

    def test_generate_birthdays(self):
        number = 5
        birthdays = generate_birthdays(number)

        # Check if the returned value is a list
        self.assertIsInstance(birthdays, list)

        # Check if the length of the list is equal to the given number
        self.assertEqual(len(birthdays), number)

    # @patch("builtins.input", side_effect=["abc", "1", "101", "5"])
    # def test_validate_input(self, mock_input):
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         number = validate_input()

    #         self.assertEqual(number, 5)  # Check if the returned number is correct

    #         expected_output = (
    #             "\n⚠️⚠️  Please enter a number  ⚠️⚠️\n"
    #             "\n⚠️⚠️  Minimum 2, Maximum 100  ⚠️⚠️\n"
    #         )
    #         self.assertEqual(
    #             output.getvalue(), expected_output
    #         )  # Check the printed output

    def test_find_first_duplicate(self):
        dates = [
            "Feb 28",
            "Jun 30",
            "Jun 10",
            "Jun 9",
            "Oct 10",
            "Oct 15",
            "Aug 7",
            "Jun 29",
            "Sep 24",
            "Nov 12",
            "Apr 23",
            "May 25",
            "May 4",
            "Feb 2",
            "Oct 7",
            "Mar 16",
            "Jul 16",
            "Mar 3",
            "Dec 8",
            "Apr 18",
            "Jun 4",
            "Jul 13",
            "Sep 26",
            "Jul 24",
            "Jul 12",
            "Apr 2",
            "Sep 1",
            "Dec 7",
            "Apr 4",
            "Nov 27",
            "Apr 18",
            "Oct 24",
        ]

        result = find_first_duplicate(dates)

        self.assertEqual(result, "Apr 18")  # Check if the first duplicate is returned


if __name__ == "__main__":
    unittest.main()
