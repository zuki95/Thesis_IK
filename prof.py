import csv
import sys
import pandas as pd
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from profanityfilter import ProfanityFilter
import re
import requests


def main(argv):
	with open(sys.argv[1],'r') as inputfile, open(sys.argv[2],'a') as outputfile:
		df = pd.read_csv(inputfile)
	#return df



#def check_profanity(df):
	pf = ProfanityFilter()
	profanity = []
	for row in df['body']:
		prof = pf.is_clean(row)
		profanity.append(prof)

	df['profanity'] = profanity

	df.to_csv(outputfile)


if __name__ == "__main__":
	main(sys.argv)