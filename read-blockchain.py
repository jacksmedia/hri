# python3 read-blockchain.py --ticker COMBEYS-bc640d
# python3 read-blockchain.py --ticker COMBOTS-aa4150
# use in a python3 env w line 1 (example^^, change ticker to modify MvX collection grabbed)
# takes blockchain snapshot & creates:
# file 1) per nft = each NFTs' name + owner wallet address (.csv file w timestamp)
# file 2) sums of NFTs per holders' wallets (.txt file w timestamp)
# file 3) identical data as 2, in '-amt-per-holder.csv' (overwrites this file each run! Intended for distro use)
import argparse
import csv
import requests
import time

from datetime import datetime
from pathlib import Path

# Timer
seconds = time.time()
local_time = time.ctime(seconds)
current_date = datetime.now()

# Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--ticker", help="Ticker of the collection", required=True)
args = parser.parse_args()

# Constants
FRAMEIT_WALLET_ADDRESS = "erd1qqqqqqqqqqqqqpgq705fxpfrjne0tl3ece0rrspykq88mynn4kxs2cg43s"
XOXNO_WALLET_ADDRESS = "erd1qqqqqqqqqqqqqpgq6wegs2xkypfpync8mn2sa5cmpqjlvrhwz5nqgepyg8"
KROGAN_SWAP_WALLET_ADDRESS = "erd1qqqqqqqqqqqqqpgq8xwzu82v8ex3h4ayl5lsvxqxnhecpwyvwe0sf2qj4e"
DEAD_RARE_WALLET_ADDRESS = "erd1qqqqqqqqqqqqqpgqd9rvv2n378e27jcts8vfwynpx0gfl5ufz6hqhfy0u0"
ISENGARD_WALLET_ADDRESS = "erd1qqqqqqqqqqqqqpgqy63d2wjymqergsxugu9p8tayp970gy6zlwfq8n6ruf"

# creates 'black listed' array so these addresses don't get included
black_listed_addresses = [FRAMEIT_WALLET_ADDRESS,
                                    XOXNO_WALLET_ADDRESS,
                                    KROGAN_SWAP_WALLET_ADDRESS,
                                    DEAD_RARE_WALLET_ADDRESS,
                                    ISENGARD_WALLET_ADDRESS]

nft_collection_name = args.ticker
values = []
single_wallet = []
all_wallets = []

# output files' name creation
snapshot_file = current_date.strftime(f"%H-%M-%S-%b-%d-%Y-snapshot-{nft_collection_name}.txt")
per_holder = current_date.strftime(f"{nft_collection_name}-amt-per-holder")
per_nft = current_date.strftime(f"{nft_collection_name}.csv")

# query blockchain
i = 0
while i < 10000:
    nfts = requests.get(f'https://api.multiversx.com/collections/{nft_collection_name}/nfts?from=' + str(
        i) + '&size=100&withOwner=true').json()
    for nft in nfts:
        print(f'Logging NFT: {nft["name"]}') # shows the onchain 'name' metadata in terminal while running
        try: 
            if nft["owner"]:
                print(f'owned by: {nft["owner"]}') # shows the onchain 'owner' metadata in terminal while running
                with open(per_nft, "a") as f: # writes this to 'wallet-per-NFT' file
                    f.write(f'{nft["name"]},{nft["owner"]}\n')
        except:
            print('No owner data')
            with open(per_nft, "a") as f: # prints this if no owner metadata found
                f.write(f'{nft["name"]},"No owner data"\n') # writes this to 'wallet-per-NFT' file
        try:
            if nft["owner"] not in single_wallet:
                single_wallet.append(nft["owner"])
            all_wallets.append(nft["owner"])
        except:
            pass
    i = i + 100

# Collection-wide stats calculations
for wallet in single_wallet: 
    if wallet not in black_listed_addresses:
        value = {"owner": wallet, "nftsCount": all_wallets.count(wallet)}
        values.append(value)

# Create outputs
json_snapshot = "{}".format(snapshot_file) # 1st output: holders as json items, in text file

p = Path('.')
p.mkdir(parents=True, exist_ok=True)
func_txt = open(json_snapshot, "w") # writing vs appending; w wipes & a adds

values.sort(key=lambda x: x.get('nftsCount'), reverse=True) # bubbles the largest hodlers to top of list

with open(current_date.strftime(f"{per_holder}.csv"), "wt") as outputcsvfile: # 2nd output: csv of holders
    writer = csv.writer(outputcsvfile, delimiter=",")
    writer.writerow(["Address", "Count"])  # write header
    for output in values:
        func_txt.write(output.__str__() + "\n")
        writer.writerow([output['owner'], output['nftsCount']])

# Compute useful info
total_nft = 0
average = 0

for nft in range(0, len(values)):
    total_nft = total_nft + values[nft]['nftsCount']

average = round(total_nft / len(values), 2)

print(f'\n----- Trust J4cks & DYOR fren -----\n')
print(f'Successfully created your CSV & txt files for MX collection {nft_collection_name}') # tells user what happened (UI)
print(f'Number of Wallets with {nft_collection_name}: {len(values)}')
print(f'Number of NFTs not on marketplaces: {total_nft}\n')
print(f'Average Number of NFTs per wallet {average}\n')
print("Local Earth time is now:", local_time)
print(f'Your backup of this snapshot is in file: {snapshot_file}')
print(f'Your tabular data is in file: {per_holder}.csv')
print(f'\n----- Thank you for using Jacks.media scripts -----\n')