import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.date.today()
        future_date = current_date + datetime.timedelta(days=days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer for days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
