import csv  # Import the CSV module to work with CSV files
from datetime import datetime  # Import datetime (can be used later for automatic date)

# File where the work hours will be stored
file_name = "data.csv"

# Function to write data to the CSV file
def write_to_csv(data):
    try:
        # Open the CSV file in append mode ("a") to add new rows
        # newline="" prevents extra blank lines between rows
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)  # Create a CSV writer
            writer.writerow(data)  # Add the new row to the file
    except Exception as e:
        # Print error message if saving fails
        print("Error saving data:", e)

# Function to ask the user for input
def get_input():
    name = input("What is your name? ")  # Ask for name
    date = input("Date (YYYY-MM-DD): ")  # Ask for date
    hours = input("Number of hours worked: ")  # Ask for hours worked
    project = input("Which project did you work on? ")  # Ask for project

    # Return all answers as a list
    return [name, date, hours, project]

# Main program
def main():
    print("=== Work Hours Registration System ===")  # Introduction for the user

    data = get_input()  # Get input from the user
    write_to_csv(data)  # Save the data to CSV

    print("Data saved!")  # Confirmation

# Ensures the program only runs when executed directly
if __name__ == "__main__":
    main()