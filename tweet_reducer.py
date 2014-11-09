#!/usr/bin/python

#################################################
#																								#
#		tweet_reducer.py														#
#		Created by Kim Ngo on Oct. 9, 2014					#
#																								#
#		Reducer that reads in a key and value list	#
#		for Hadoop MapReduce												#
#		(key, values) = (hashtag, timestamps)				#
#																								#
#		Reduces to (hashtag, "timestamp, count")		#
#		where timestamp is in bins of 10 mins				#
#																								#
#################################################

import fileinput
import sys
import re
import string
from collections import OrderedDict

BIN = 15
KEY, VALUE = range(2)
hashtag_dict = dict()


for line in fileinput.input():
	line = line.rstrip()	# Removes carriage return
	
	# Unique key = #prayforboston	2013 4 15 21:1
	key = line[:-4]
	
	if key not in hashtag_dict:
		hashtag_dict[key] = int()
	
	hashtag_dict[key] += 1
	#print key, hashtag_dict[key]

# Orders by timestamp
hashtag_ordered = OrderedDict(sorted(hashtag_dict.items()))

for h in hashtag_ordered:
	print h + "\t" + str(hashtag_ordered[h])
		
		
