#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Parameters:
    csv_filename (str): The name of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    success = convert_csv_to_json('example.csv')
    if success:
        print("CSV file was successfully converted to JSON.")
    else:
        print("Failed to convert CSV file to JSON.")

