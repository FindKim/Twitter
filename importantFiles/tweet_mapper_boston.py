#!/usr/bin/python

#################################################
#																								#
#		tweet_mapper.py															#
#		Created by Kim Ngo on Oct. 9, 2014					#
#																								#
#		Reads in a line of tweet from Twitter API		#
#		Parses tweet by hashtag and timestamp				#
#																								#
#		tailored for boston dataset: " "						#
#		timestamp: Mon, 15 Apr 2013 21:11:17 +0000	#
#																								#
#		emits (key, value) = (hashtag, timestamp)		#
#																								#
#################################################


import fileinput
import sys
import re
import string
import unicodedata

bins_per_hour = 6;
bins_per_year = 52560;

# Function converts timestamp of API tweet: Mon, 15 Apr 2013 21:11:17 +0000
# To 2013 4 15 21:11:17
WEEKDAY, DAY, MONTH, YEAR, TIME, MISC = range(6)	# 0, 1, 2, 3, 4, 5
def convert_timestamp(ts):
	try:
		convert_timestamp.calls++;
	except AttributeError:
		convert_timestamp.calls = 1;

	days_before = 0;
	bins_since_0_hour = 0;
	month = str()
	ts = ts.split()	# Split by space
	
	#tweets MUST come in in chronological order
	if convert_timestamp.calls == 1:   # save the year for future reference if this is the first call 
		convert_timestamp.zero_year = int(ts[YEAR]);
	
	if ts[MONTH] == 'Jan':
		days_before = 0;
		month = '01'
	elif ts[MONTH] == 'Feb':
		days_before = 31;
		month = '02'
	elif ts[MONTH] == 'Mar':
		days_before = 59;
		month = '03'
	elif ts[MONTH] == 'Apr':
		days_before = 90;
		month = '04'
	elif ts[MONTH] == 'May':
		days_before = 120;
		month = '05'
	elif ts[MONTH] == 'Jun':
		days_before = 151;
		month = '06'
	elif ts[MONTH] == 'Jul':
		days_before = 181;
		month = '07'
	elif ts[MONTH] == 'Aug':
		days_before = 212;
		month = '08'
	elif ts[MONTH] == 'Sep':
		days_before = 243;
		month = '09'
	elif ts[MONTH] == 'Oct':
		days_before = 273;
		month = '10'
	elif ts[MONTH] == 'Nov':
		days_before = 304;
		month = '11'
	elif ts[MONTH] == 'Dec':
		days_before = 334;
		month = '12'
	else:
		print "Error with " + ts[MONTH]

	#figure out time bins from 0 hour
	time = ts[TIME].split(':')
	bins_since_0_hour += bins_per_hour * int(time[0]) + int(time[1][:-1]);

	bins_since_0_hour += 24 * bins_per_hour * (days_before + int(ts[DAY]) - 1);
	
	bins_since_0_hour += (int(ts[YEAR]) - convert_timestamp.zero_year) * bins_per_year;

	since_leap_year = convert_timestamp.zero_year % 4;
	leap_years_past = int( (int(ts[YEAR]) - convert_timestamp.zero_year) / 4);
	if( ((int(ts[YEAR]) - convert_timestamp.zero_year) % 4) + since_leap_year >= 4):
		leap_years_past++;
		
	bins_since_0_hour += 24 * bins_per_hour * leap_years_past;
	ts = ts[YEAR] + " " + month + " " + ts[DAY] + " " + ts[TIME]
	
	return bins_since_0_hour


# Regex hashtag pattern
hashtag_pattern = re.compile('^#')

# Parses line into (key, value)
for line in fileinput.input():
	line = line.rstrip()	# Removes carriage return
	
	tweetAPI = re.search('\"text\": \".*?\"', line)
	
	# Parses only text of tweet
	if tweetAPI:
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
