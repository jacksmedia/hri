import csv

def join_csv(csv1_path, csv2_path, output_path):
    # Read the first CSV file and create a dictionary based on the common column
    csv1_data = {}
    with open(csv1_path, 'r') as csv1_file:
        csv1_reader = csv.DictReader(csv1_file)
        for row in csv1_reader:
            csv1_data[row['edition']] = row

    # Open the second CSV file and append the data from csv2['rank'] to csv1
    with open(csv2_path, 'r') as csv2_file:
        csv2_reader = csv.DictReader(csv2_file)
        for row in csv2_reader:
            common_value = row['edition']
            if common_value in csv1_data:
                csv1_data[common_value]['rank'] = row['rank']

    # Write the joined data to a new CSV file
    with open(output_path, 'w', newline='') as output_file:
        fieldnames = csv1_reader.fieldnames + ['rank']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv1_data.values())

# Usage example
csv1_path = 'COMBEYS-bc640d.csv'
csv2_path = 'combeys.csv'
output_path = 'combeys-holders-ranks.csv'

join_csv(csv1_path, csv2_path, output_path)