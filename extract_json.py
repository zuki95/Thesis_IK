
import sys
import json

#command multiple files: python3 pipe.py RC_2015-10 output.txt | python3 pipe.py RC_2014-01 output2.txt

#python3 pipe.py oefen.json uit.txt 1233446401 1233446693 | python3 pipe.py oefen1.json uit1.txt 1233446769 1233446962



def main(argv):

	with open(sys.argv[1],'r') as reddit_file, open(sys.argv[2],"a") as outputfile:

		#reddit_file = open("RC_2015-10", "r")
		#outputfile= open("08102015.txt", "a")
		for line in reddit_file:
			try:
				comment = json.loads(line)
				reddit_comments = json.dumps(comment['body'])
			
				epochtime = json.loads(line)
				reddit_time = json.dumps(int(epochtime['created_utc']))

				parent = json.loads(line)
				parent_ID = json.dumps(parent['parent_id'])


				scores = json.loads(line)
				reddit_score = json.dumps(scores['score'])

				subreddit = json.loads(line)
				sub_reddit = json.dumps(subreddit['subreddit'])

				link = json.loads(line)
				link_ID = json.dumps(link['link_id'])

				edit = json.loads(line)
				edited = json.dumps(edit['edited'])

			
				for edited_comment in edited.split():
					if edited_comment in ['false']:
						for term in reddit_comments.split():
							if term in ['Bitcoin','bitcoin']:
								for time in reddit_time.split():
									if int(sys.argv[3]) <= int(time) <= int(sys.argv[4]):
										outputfile.write(reddit_time+','+reddit_comments+','+parent_ID+','+link_ID+','+reddit_score+','+sub_reddit+'\n')
			


			#for word,time in zip(reddit_comments.split(),reddit_time.split()):
			#	if word in ['Downvoting'] and 1233446399 <= int(time) <= 1233446662:
			#		print(time,reddit_comments,parent_comments,reddit_score,sub_reddit)
				#if word in ['tastes', 'donuts', 'people', 'dolphins', 'bandwagon', 'dollar', 'keyboard'] and 1233446400 <= int(time[0:10]) <= 1233446662:
					#for father in parent_comments.split():
						#if father[:3] == '"t3':
							#print(parent_comments+':'+reddit_comments+':'+reddit_link+':'+reddit_score+'\n')#+':'+reddit_time+':'+reddit_title+':'+reddit_link+'\n')
							#continue
				#	outputfile.write(parent_comments+'\n')
					
			#for word in reddit_comments.split():
			#	if word in ['bitcoin','btc','crypto','satoshi']:
			#		outputfile.write(reddit_comments+'\n')
			#for time in reddit_time.split():
			#	if 1384214400 <= int(time[0:10]) <= 1384300799:
			#		outputfile.write(reddit_time+':'+reddit_comments+'\n')
			#		continue
					
			except:
				continue	
		outputfile.close()

if __name__ == "__main__":
	main(sys.argv)