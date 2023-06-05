import pandas as pd
import csv

#inputs to combine
csv1 = pd.read_csv('./golden-beys.csv')
csv2 = pd.read_csv('./COMBEYS-bc640d.csv')
# output
output_file = 'combeys-holders-ranks.csv'

# combine all rows by 'edition' value, right vs inner bc idk!
output = pd.merge(csv1, csv2,
						on='edition',
						how='right')
# Save to CSV
output.to_csv('./merged-combey.csv', index=False)

