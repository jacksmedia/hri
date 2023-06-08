import csv
from collections import defaultdict

def sum_and_count_values(csv_file):
    # Read the CSV file into a dictionary of lists
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Create a dictionary to store the sums and counts
    sum_counts = defaultdict(lambda: [0, 0])  # [Sum, Count]

    # Calculate the HRI
    for row in rows[1:]:
        key = row[1] # owner is the key value
        value = int(row[2]) # the rank in the NFT collection
        sum_counts[key][0] += value  # Sum = running total of all rank values
        sum_counts[key][1] += 1      # Count aka Total Comboeys: is assigned to each owner bc that's our primary key
        # Do the Comverse special maths to calculate HRI
        # 1. Divide the Sum by Count, get Average
        sum_counts[key][0] = sum_counts[key][0]/sum_counts[key][1]
        # 2. Divide Average by 2x count
        sum_counts[key][0] = sum_counts[key][0]/(sum_counts[key][1]*2)
        # 3. if NFT count < 10, incur HRI balance penalty
        if sum_counts[key][1] < 10:
            sum_counts[key][0] = sum_counts[key][0] + (10 - sum_counts[key][1])

    # Create the new CSV file with three columns
    new_csv_file = 'HRI_combeys.csv'
    with open(new_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Holder', 'HRI', 'Combeys'])
        for key, (sum_val, count) in sum_counts.items():
            writer.writerow([key, sum_val, count])

    return new_csv_file

# Usage example
csv_file = './combeys-holders-ranks.csv'
new_csv_file_path = sum_and_count_values(csv_file)
print(f"New CSV file created: {new_csv_file_path}")