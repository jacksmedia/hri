import pandas as pd
import csv

#inputs to combine
csv1 = pd.read_csv('./golden-bots.csv')
csv2 = pd.read_csv('./COMBOTS-aa4150.csv')
# output
output_file = 'combots-holders-ranks.csv'

# combine all rows by 'edition' value, inner bc only want exact matches
output = pd.merge(csv1, csv2,
						on='edition',
						how='inner')
# Save to CSV
output.to_csv('./merged-combot.csv', index=False)
