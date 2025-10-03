from datetime import datetime


def main():
    while True:
        input_date = input("Enter a date in format 'YYYY-MM-DD': ")
        result = get_days_from_today(input_date)
        print(result)
        if "Invalid date" not in result:
            break


def get_days_from_today(date_str: str) -> str:

    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = (today - input_date).days

        if difference > 0:
            return f"The date was {difference} days ago"
        elif difference < 0:
            return f"The date will be in {-difference} days"
        else:
            return "The date is today"

    except ValueError:
        return "Invalid date. Please use the format 'YYYY-MM-DD'."


main()
