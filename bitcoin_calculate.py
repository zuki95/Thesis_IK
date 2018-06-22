import csv

import pandas as pd


def calculate_change_btc():
	with open("bitcoin_dataset1.csv") as csvfile:
		reader = csv.reader(csvfile)
		
		for row in reader:
			if row[2] == "Open":
				continue
			elif row[4] == "Close":
				continue
			
			else:
				opening = float(row[1])
				closing = float(row[4])
				#print(row[0], opening, closing)
				difference = ((closing - opening)/opening)*100.0
				if difference > 10: #if price change more than 10 percent within 24hr
					print(row[0],"{0:.2f}".format(round(difference,2)))
					
				

calculate_change_btc()