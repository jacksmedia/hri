import csv
from collections import defaultdict

def sum_and_count_values(csv_file):
    # Read the CSV file into a dictionary of lists
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Create a dictionary to store the sums and counts
    sum_counts = defaultdict(lambda: [0, 0])  # [Sum, Count]

    # Calculate the sums and counts
    for row in rows[1:]:
        key = row[0]
        value = int(row[1])
        sum_counts[key][0] += value  # Sum
        sum_counts[key][1] += 1      # Count aka Total Combots
        # Do the Comverse special maths to calculate HRI
        # 1. Divide the sum by count, get average
        sum_counts[key][0] = sum_counts[key][0]/sum_counts[key][1] 
        # 2. Divide average by 2x count
        sum_counts[key][0] = sum_counts[key][0]/(sum_counts[key][1]*2)
        # 3. if NFT count < 10, incur HRI balance penalty
        if sum_counts[key][1] < 10 : sum_counts[key][0] = sum_counts[key][0] + 10 - sum_counts[key][1]

    # Create the new CSV file with three columns
    new_csv_file = 'HRI_combots.csv'
    with open(new_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Holder', 'sum', 'Combots'])
        # writer.writerow(['Holder', 'HRI', 'Combots'])
        for key, (sum_val, count) in sum_counts.items():
            writer.writerow([key, sum_val, count])

    return new_csv_file

# Usage example
csv_file = './merged-combot.csv'
new_csv_file_path = sum_and_count_values(csv_file)
print(f"New CSV file created: {new_csv_file_path}")
