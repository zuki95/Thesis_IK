

import os
import glob
import sys
import csv

import pandas as pd

def main():
	
	results = pd.DataFrame([])
	for counter, file in enumerate(glob.glob("final_*")):
		namedf = pd.read_csv(file, skiprows=0)
		results = results.append(namedf)
	
	results.to_csv('final.csv')

main()