import random
import calendar


YEAR = 2023


def get_random_birthday():
    """
    Return a random Month and Day eg. 'Jan 21' , 'May 8'
    """

    # get a random month
    month = random.randint(1, 12)

    # get the nimber of days in that month
    days = calendar.monthrange(year=YEAR, month=month)[1]

    # get a random day from that month
    day = random.randint(1, days)

    # get the month abbr name
    month_name = calendar.month_abbr[month]

    return f"{month_name} {day}"


def generate_birthdays(number):
    """Returns a list of birthdays for the given number"""

    birthdays = [get_random_birthday() for _ in range(number)]
    return birthdays


def validate_input():
    """Ensure user inputs a Positive Integer"""

    while True:
        try:
            print("How many Birthdays should I generate?")
            number = int(input("> "))
            if number > 0:
                return number
            else:
                print("\n⚠️⚠️  The Number must be positive  ⚠️⚠️\n")
        except ValueError:
            print("\n⚠️⚠️  Please enter a number  ⚠️⚠️\n")


def main():
    number = validate_input()
    print(generate_birthdays(number))


if __name__ == "__main__":
    main()
