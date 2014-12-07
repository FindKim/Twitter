#!/usr/bin/python

#################################################
#																								#
#		tweet_reducer.py														#
#		Created by Kim Ngo on Oct. 9, 2014					#
#		Assisted by Ryan Boccabella									#
#																								#
#		Reducer that reads in a key and value list	#
#		for Hadoop MapReduce												#
#		(key, values) = (hashtag, timestamps)				#
#																								#
#		Reduces to (hashtag, "timestamp, count")		#
#		where timestamp is in bins of 10 mins				#
#		Reducer for first stage of MapReduce				#
#################################################

import fileinput
import sys
import re
import string
from collections import OrderedDict

KEY, VALUE = range(2)
hashtag_dict = dict()

for line in fileinput.input():
	line = line.rstrip()	# Removes carriage return
	
	# Unique key = #prayforboston	timefrom0hour
	key = line
	
	#if it's not present, initialize it to 0
	if key not in hashtag_dict:
		hashtag_dict[key] = int()
	
	hashtag_dict[key] += 1

# Orders by timestamp
hashtag_ordered = OrderedDict(sorted(hashtag_dict.items()))

#Emit the map as a tab delimited triple
for h in hashtag_ordered:
	print h + "\t" + str(hashtag_ordered[h])
		
		
