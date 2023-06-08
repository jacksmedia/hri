# python3 swap-cols.py --input COMBEYS-bc640d.csv
# python3 swap-cols.py --input COMBOTS-aa4150.csv
import csv
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file", required=True)
args = parser.parse_args()
csv_file = args.input

def swap_columns(csv_file):
    # Read the CSV file into a list of rows
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    data = rows[0:] # every row in the csv file

    # Swap the values in columns A and B
    swapped_data = [[row[1], row[0]] for row in data]

    # Write  swapped rows back into the csv file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(swapped_data)

swap_columns(csv_file)
print(f'\n----- Trust J4cks & DYOR fren -----\n')
print(f'Successfully swapped Columns A & B in {csv_file} .')
print(f'\n----- Thank you for using Jacks.media scripts -----\n')