#!/usr/bin/python

#################################################
#																								#
#		tweet_mapper_boston.py											#
#		Created by Kim Ngo on Oct. 9, 2014					#
#		Assisted by Ryan Boccabella									#							
#                                               #
#		Reads in a line of tweet from Twitter API		#
#		Parses tweet by hashtag and timestamp				#
#																								#
#		tailored for boston dataset: " "						#
#		timestamp: Mon, 15 Apr 2013 21:11:17 +0000	#
#																								#
#		emits (key, value) = (hashtag, timestamp)		#
#		mapper for first round of mapreduce 				#
#################################################


import fileinput
import sys
import re
import string
import unicodedata

#based on 10 minute time bin
bins_per_hour = 6;
bins_per_year = 52560;

# Function converts timestamp of API tweet: Mon, 15 Apr 2013 21:11:17 +0000
# To 2013 4 15 21:11:17
WEEKDAY, DAY, MONTH, YEAR, TIME, MISC = range(6)	# 0, 1, 2, 3, 4, 5
def convert_timestamp(ts):
	try:
		convert_timestamp.calls+=1;
	except AttributeError:
		convert_timestamp.calls = 1;

	days_before = 0;
	bins_since_0_hour = 0;
	month = str()
	ts = ts.split()	# Split by space
	
	#tweets MUST come in in chronological order
	if convert_timestamp.calls == 1:   # save the year for future reference if this is the first call 
		convert_timestamp.zero_year = int(ts[YEAR])
	
	#keep track of the days prior to the start of this in order to calculate time bins
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

	if( (int(ts[YEAR]) % 4) == 0 and days_before > 31):
		days_before+=1;  #account for leap year

	#figure out time bins from 0 hour, which is 12:00am January 1 of year of first hashtag
	time = ts[TIME].split(':')
	
	#adds the number of hours * bins per hour, + the number of minutes by just looking at the 10s place
	bins_since_0_hour += bins_per_hour * int(time[0]) + int(time[1][:-1]);

	#24 hours per day, times days, time bins per hour gives bins 
	bins_since_0_hour += 24 * bins_per_hour * (days_before + int(ts[DAY]) - 1);
	
	#if you've changed years since the 0 hour, add the number of bins in a year
	bins_since_0_hour += (int(ts[YEAR]) - convert_timestamp.zero_year) * bins_per_year;

	#account for leap years
	since_leap_year = convert_timestamp.zero_year % 4;
	leap_years_past = int( (int(ts[YEAR]) - convert_timestamp.zero_year) / 4);
	if( ((int(ts[YEAR]) - convert_timestamp.zero_year) % 4) + since_leap_year >= 4):
		leap_years_past+=1;
	bins_since_0_hour += 24 * bins_per_hour * leap_years_past;

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
			all_ts = re.findall('\"created_at\": \".*?\"', line)
			which_ts = len(all_ts)
			timestamp = all_ts[which_ts-1]
			timestamp = timestamp.split('": "')[1]
			timestamp = timestamp.strip('\'');
			timestamp = convert_timestamp(timestamp)
		
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
								print '#' + w.lower() + '\t' + str(timestamp)
