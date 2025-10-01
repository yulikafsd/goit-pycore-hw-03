from datetime import datetime

def main() -> str:
    while True:
        date_input = input("Enter a date in format 'YYYY-MM-DD': ")
        result = get_days_from_today(date_input)
        print(result)
        if "Invalid date" not in result:
            break

def get_days_from_today(date) -> str:

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = (today - date_obj).days

        if difference > 0:
            return f"The date was {difference} days ago"
        elif difference < 0:
            return f"The date will be in {-difference} days"
        else:
            return "The date is today"

    except ValueError:
        return "Invalid date. Please use the format 'YYYY-MM-DD'."

main()