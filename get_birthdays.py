from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:

    # Create list for upcoming birthdays
    upcoming_birthdays = []

    # Check today's date
    today = datetime.today().date()

    # Check every birthday and add to the list of upcoming birthdays
    for user in users:

        # Turn birthday string into a date object
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = birthday_date.replace(year=today.year)

        # If bd this year passed, change year to the next one
        if congratulation_date < today:
            congratulation_date = birthday_date.replace(year=(today.year + 1))

        # Check if bd is in the following 7 days
        delta = (congratulation_date - today).days

        if delta <= 7:  # Check if BD is today? 1 <= delta <= 7

            # Check if congratulation weekday is Sat or Sun:
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Parse date to format YYYY.MM.DD
            parsed_date = congratulation_date.strftime("%Y.%m.%d")

            # Add dictionary with name and congratulation date to the upcoming birthdays list
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": parsed_date}
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.10.03"},
    {"name": "Saturday Man", "birthday": "1987.10.04"},
    {"name": "Sunday Man", "birthday": "1995.10.05"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
