from random import sample


# Main function, that asks for the min, max and quantity of numbers to generate:
def main():
    while True:

        # Get user input
        input_conditions = input(
            "Enter diapason and quantity of numbers you'd like to generate\n"
            "in format 'min, max, quantity' (comma-separated integers): "
        )
        try:
            # Split the input string and convert to integers
            min, max, quantity = map(int, input_conditions.split(","))

            # Call the function and print the result
            result = get_numbers_ticket(min, max, quantity)
            print(result)

        # Handle invalid input format (non-integer values or wrong number of values):
        except ValueError:
            result = "\nInvalid input. Please enter three integers separated by commas. Try again"
            print(result)

        # Break the loop if the input was valid
        if type(result) is list:
            break


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return "\nThe diapason should be between 1 and 1000. Try again"
    elif quantity > (max - min + 1):
        return (
            f"\nCannot select {quantity} unique numbers from the given range. Try again"
        )
    elif min > max:
        return "\nThe minimum value cannot be greater than the maximum value. Try again"
    else:
        return sorted(sample(range(min, max + 1), quantity))


main()
