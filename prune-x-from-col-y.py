# python3 prune-x-from-col-y.py --input COMBEYS-bc640d.csv --prune 'Combey ' --col 0
import csv
import argparse

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file", required=True)
parser.add_argument("--prune", help="String to remove", required=True)
parser.add_argument("--col", help="Column of csv to work on", required=True)
args = parser.parse_args()
csv_file = args.input # file to work on
prune_this = args.prune # what's getting removed from the csv
prune_this = str(prune_this) #typing
this_col = args.col # what column of csv?
this_col = int(this_col) # typing

def prune_from(csv_file):
    # Read the CSV file into a list of rows
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # trim "Combey #" from values in Column B
    for row in rows[0:]:
       row[this_col] = row[this_col].replace(prune_this,'')

    # Write the trimmed rows back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

prune_from(csv_file)
print(f'\n----- Trust J4cks & DYOR fren -----\n')
print(f'Successfully trimmed {prune_this} from Column {this_col} in {csv_file} .')
print(f'\n----- Thank you for using Jacks.media scripts -----\n')