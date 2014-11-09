#!/usr/bin/python

#################################################
#																								#
#		tweet_mapper.py															#
#		Created by Kim Ngo on Oct. 9, 2014					#
#																								#
#		Reads in a line of tweet from Twitter API		#
#		Parses tweet by hashtag and timestamp				#
#																								#
#		emits (key, value) = (hashtag, timestamp)		#
#																								#
#################################################


import fileinput
import sys
import re
import string
import unicodedata


# Function converts timestamp of API tweet: Mon, 15 Apr 2013 21:11:17 +0000
# To 2013 4 15 21:11:17
WEEKDAY, DAY, MONTH, YEAR, TIME, MISC = range(6)	# 0, 1, 2, 3, 4, 5
def convert_timestamp(ts):

	month = str()
	ts = ts.split()	# Split by space
	if ts[MONTH] == 'Jan':
		month = '01'
	elif ts[MONTH] == 'Feb':
		month = '02'
	elif ts[MONTH] == 'Mar':
		month = '03'
	elif ts[MONTH] == 'Apr':
		month = '04'
	elif ts[MONTH] == 'May':
		month = '05'
	elif ts[MONTH] == 'Jun':
		month = '06'
	elif ts[MONTH] == 'Jul':
		month = '07'
	elif ts[MONTH] == 'Aug':
		month = '08'
	elif ts[MONTH] == 'Sep':
		month = '09'
	elif ts[MONTH] == 'Oct':
		month = '10'
	elif ts[MONTH] == 'Nov':
		month = '11'
	elif ts[MONTH] == 'Dec':
		month = '12'
	else:
		print "Error with " + ts[MONTH]
	
	ts = ts[YEAR] + " " + month + " " + ts[DAY] + " " + ts[TIME]
	return ts


# Regex hashtag pattern
hashtag_pattern = re.compile('^#')

# Parses line into (key, value)
for line in fileinput.input():
	line = line.rstrip()	# Removes carriage return
	
	tweetAPI = re.search('\"text\": \".*?\"', line)
	
	# Parses only text of tweet
	tweet = tweetAPI.group(0).strip('"')
	tweet = tweet.split('": "')[1]

	# Check if hashtag is within tweet text
	if (tweet.find('#') != -1):
		
		# Get timestamp
		timestampAPI = re.search('"created_at": ".*?"', line)
		timestamp = timestampAPI.group(0).strip('"')
		timestamp = timestamp.split('": "')[1]
		timestamp = convert_timestamp(timestamp)
		#print tweet, timestamp
		
		# Get all hashtags
		words = tweet.split()	# Split by space
		for idx, word in enumerate(words):
			if hashtag_pattern.match(word):
				
			
				# Emits hastag and timestamp--tab delimiter
				if hashtag_pattern.match(word):
					
					# Ignores ascii/unicode characters
					word = word.encode('ascii', 'ignore')
					word = re.sub(r'[^a-zA-Z0-9#]', '', word)
					
					# Accounts for multiple hashtags without space
					word = word.split('#')
					for w in word:
						if w != '':
							print '#' + w.lower() + '\t' + timestamp
		
		
		
