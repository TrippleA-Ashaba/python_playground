import calendar
import random

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
    """Returns a list of birthdays for the given number eg. ['Feb 28', 'Jun 30', 'Jun 10', 'Jun 9', 'Oct 10']"""

    birthdays = [get_random_birthday() for _ in range(number)]
    return birthdays


def validate_input():
    """Ensure user inputs a Positive Integer"""

    while True:
        try:
            print("How many Birthdays should I generate? (MIN 2, MAX 100)")
            number = int(input("> "))
            if 2 <= number <= 100:
                return number
            else:
                print("\n⚠️⚠️  Minimum 2, Maximum 100  ⚠️⚠️\n")
        except ValueError:
            print("\n⚠️⚠️  Please enter a number  ⚠️⚠️\n")


# def find_duplicate_dates(dates):
#     """Returns duplicate dates and number of times they occur eg. {'Sep 3': 2, 'Jun 24': 2, 'Aug 16': 2, 'Jul 17': 2}"""

#     seen = defaultdict(int)
#     duplicates = {}

#     for date in dates:
#         seen[date] += 1

#     for date, count in seen.items():
#         if count > 1:
#             duplicates[date] = count

#     return duplicates


def find_first_duplicate(dates):
    """Return on the first instance of a duplicate birthday"""

    if len(dates) == len(set(dates)):
        return None

    seen = set()

    for date in dates:
        if date in seen:
            return date
        seen.add(date)


def main(num_of_simulations):
    number = validate_input()
    matches = 0

    for i in range(num_of_simulations):
        birthdays = generate_birthdays(number)
        dupe = find_first_duplicate(birthdays)

        if dupe:
            matches += 1

        if i % 10_000 == 0:
            print(f"{i} Simulations ran ....")
            print("Simulating...")
            print()

    probability_of_matching_birthdays = (matches / num_of_simulations) * 100

    print(f"Simulation ran < {num_of_simulations} > times")
    print(f"Similar Birthdays occurred < {matches} > times")
    print(
        f"Probability of matching birthdays in a group of < {number} > people is < {probability_of_matching_birthdays} >"
    )


if __name__ == "__main__":
    main(100_000)
