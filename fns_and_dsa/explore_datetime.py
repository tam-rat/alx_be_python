# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    # Prompt the user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Get the current date
    current_date = datetime.now()

    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)

    # Print the formatted future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
