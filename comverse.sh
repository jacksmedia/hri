rm COMB* # to prevent line 5 & 7 from adding 4 headers per day >_<
sleep 2 # superstition ngl >_<
python3 read-blockchain.py --ticker COMBEYS-bc640d # creates COMBEYS-bc640d.csv
sleep 12 # prevent timeouts to this IP
python3 read-blockchain.py --ticker COMBOTS-aa4150 # creates COMBOTS-aa4150.csv
sleep 2 # superstition ngl >_<
echo edition,owner > table-header.csv && cat COMBEYS-bc640d.csv >> table-header.csv && mv table-header.csv ./COMBEYS-bc640d.csv
sleep 2 # superstition ngl >_<
echo edition,owner > table-header.csv && cat COMBOTS-aa4150.csv >> table-header.csv && mv table-header.csv ./COMBOTS-aa4150.csv
sleep 2 # superstition ngl >_<
python3 prune-x-from-col-y.py --input COMBEYS-bc640d.csv --prune 'Combey ' --col 0
sleep 2 # superstition ngl >_<
python3 prune-x-from-col-y.py --input COMBOTS-aa4150.csv --prune 'Combot #' --col 0
sleep 2 # superstition ngl >_<
python3 find-combey-ranks.py  # creates combeys-holders-ranks.csv
sleep 2 # superstition ngl >_<
python3 find-combot-ranks.py  # creates combots-holders-ranks.csv
sleep 2 # superstition ngl >_<
python3 hri-maths-combeys.py 
sleep 2 # superstition ngl >_<
python3 hri-maths-combots.py
