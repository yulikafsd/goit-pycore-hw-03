from datetime import datetime


# Main function, that keeps asking for a date until a valid one is provided
def main():
    while True:

        # Get user input
        input_date = input("Enter a date in format 'YYYY-MM-DD': ")
        # Call the function and print the result
        result = get_days_from_today(input_date)
        print(result)

        # Break the loop if the input was valid
        if "Invalid date" not in result:
            break


# Function to calculate the difference in days from today
def get_days_from_today(date_str: str) -> str:

    # Try to parse the date and calculate the difference
    try:

        # Parse the input date and get only date part
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Get today's date and get only date part
        today = datetime.today().date()
        # Calculate the difference in days
        difference = (today - input_date).days

        # Return the appropriate message based on the difference
        if difference > 0:
            return f"The date was {difference} days ago"
        elif difference < 0:
            return f"The date will be in {-difference} days"
        else:
            return "The date is today"

    # Handle invalid date format
    except ValueError:
        return "Invalid date. Please use the format 'YYYY-MM-DD'."


main()
