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

#def calculate_sentiment(df):
		analyser = SentimentIntensityAnalyzer()
		sentiment_s = []
		for row in df['body']:
			value = analyser.polarity_scores(row)
			sentiment_s.append(value['compound'])

		df['sentiment'] = sentiment_s
	#return df


#def check_profanity(df):
#	pf = ProfanityFilter()
#	profanity = []
#	for row in df['body']:
#		prof = pf.is_clean(row)
#		profanity.append(prof)
#
#	df['profanity'] = profanity
#	return df

#def write_csv(df):
	#df.to_csv(outputfile)
	#outputfile.close()









#def check_happy():
		hap_smiley = []
		smileys = (":)","=)")
		for row in df['body']:
			if any(s in row for s in smileys):
				hap_smiley.append(1)
			else:
				hap_smiley.append(0)

		df['smiley_pos'] = hap_smiley
	#return

#def check_unhappy():
		sad_smiley = []
		smiley = (":(","=(")
		for row in df['body']:
			if any(s in row for s in smiley):
				sad_smiley.append(1)
			else:
				sad_smiley.append(0)

		df['smiley_neg'] = sad_smiley
	#return

#def check_cryptoT1():
		terms = []
		strings = ("FOMO","fomo","Fomo")
		for row in df['body']:
			if any(s in row for s in strings):
				terms.append(1)
			else:
				terms.append(0)

		df['FOMO'] = terms
	#return

#def check_cryptoT2():
		terms1 = []
		strings1 = ("HODL","hodl","Hodl")
		for row in df['body']:
			if any(s in row for s in strings1):
				terms1.append(1)
			else:
				terms1.append(0)

		df['HODL'] = terms1
	#return

#def check_cryptoT3():
		terms2 = []
		strings2 = ("FUD","fud","Fud")
		for row in df['body']:
			if any(s in row for s in strings2):
				terms2.append(1)
			else:
				terms2.append(0)

		df['FUD'] = terms2
	#return

#def check_cryptoT4():
		terms3 = []
		strings3 = ("MOON","moon","Moon")
		for row in df['body']:
			if any(s in row for s in strings3):
				terms3.append(1)
			else:
				terms3.append(0)

		df['MOON'] = terms3
	#return

#def check_question():
		question = []
		for row in df['body']:
			if "?" in row:
				question.append(1)
			else:
				question.append(0)

		df['question'] = question
	#return

		has_url = []
		urls = ("www", "https", "http", "Http", "Https", ".com", ".org") 
		for row in df['body']:
			if any(s in row for s in urls):
				has_url.append(1)
			else:
				has_url.append(0)

		df['URL'] = has_url

		pump = []
		for row in df['body']:
			pump.append(1)

		idx = 0
		df.insert(loc=idx, column='pump', value=pump)


		df.to_csv(outputfile)


if __name__ == "__main__":
	main(sys.argv)

'''

def check_url():
	url = []
	for row in df['body']:
		if "https://" in row:
			url.append(1)
		else:
			url.append(0)

	df['url'] = url
	return

def calculate_responsetime():
	r = []
	for row in df['parent_id']:
		if row.startswith("t1_"):
			request.get(https://api.pushshift.io/reddit/comment/search?ids=comment_id)


	return responsetime 

	
'''


	

