rm COMB* # to prevent line 5 & 7 from adding 4 headers per day >_<
python3 read-blockchain.py --ticker COMBEYS-bc640d # creates COMBEYS-bc640d.csv
sleep 12 # prevent timeouts to this IP
python3 read-blockchain.py --ticker COMBOTS-aa4150 # creates COMBOTS-aa4150.csv
echo edition,owner > table-header.csv && cat COMBEYS-bc640d.csv >> table-header.csv && mv table-header.csv ./COMBEYS-bc640d.csv
sleep 2 # superstition ngl >_<
echo edition,owner > table-header.csv && cat COMBOTS-aa4150.csv >> table-header.csv && mv table-header.csv ./COMBOTS-aa4150.csv
python3 trim-combey-from-b.py --input COMBEYS-bc640d.csv
python3 trim-combot-from-b.py --input COMBOTS-aa4150.csv
python3 find-combey-ranks.py  # creates combeys-holders-ranks.csv
python3 find-combot-ranks.py  # creates combots-holders-ranks.csv
python3 hri-maths-combeys.py 
python3 hri-maths-combots.py
