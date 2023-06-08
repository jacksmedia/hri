# python3 trim-combey-from-b.py --input COMBEYS-bc640d.csv
import csv
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file", required=True)
args = parser.parse_args()
csv_file = args.input

excisee = 'Combey ' # what's getting removed from the csv

def swap_columns(csv_file):
    # Read the CSV file into a list of rows
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # trim "Combey #" from values in Column B
    for row in rows[0:]:
       row[1] = row[1].replace(excisee,'')

    # Write the trimmed rows back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

swap_columns(csv_file)
print(f'\n----- Trust J4cks & DYOR fren -----\n')
print(f'Successfully trimmed {excisee} from Column B in {csv_file} .')
print(f'\n----- Thank you for using Jacks.media scripts -----\n')