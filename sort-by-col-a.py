# python3 sort-by-col-a.py --input combeys-holders-ranks.csv
# python3 sort-by-col-a.py --input combots-holders-ranks.csv
import csv
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file", required=True)
args = parser.parse_args()
csv_file = args.input

def sort_csv_by_column(csv_file):
    # Read the CSV file into a list of rows
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Separate header row from data rows
    header = rows[0]
    data = rows[1:]

    # Sort data rows based on values in column A
    sorted_data = sorted(data, key=lambda row: row[0])

    # Combine header row and the sorted data rows
    sorted_rows = [header] + sorted_data

    # Write data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_rows)

sort_csv_by_column(csv_file)
print(f'\n----- Trust J4cks & DYOR fren -----\n')
print(f'Successfully sorted {csv_file} by Column A.')
print(f'\n----- Thank you for using Jacks.media scripts -----\n')