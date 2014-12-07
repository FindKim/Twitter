#!/usr/bin/python

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#this is a mapper for our final round of map reduce which looks at the prominence
#of hashtags of varying lengths. In the map phase, we take output from round 3 of
#the map reduce (that is, the ordering_reducer.pl) and output the length of the
#top n hashtags along with the number of occurrences of that hashtag. Results are
#sent to length_study_reducer.pl

import fileinput
import sys
import string

def main():
	#if(len(sys.argv) != 3):
	#	print 'Usage: ', sys.argv[0], ' [hashtags total count file] [top n hashtags]\n'
	#	sys.exit(0)
	
	#read in top n lines from file for descending popularity
	#with open(sys.argv[2], 'r') as ht_count_file:
	#	top_n_raw = [next(ht_count_file) for x in xrange(int(sys.argv[1]))]
		
	for line in fileinput.input():
		line = line.strip()
		line = line.split('\t')
		if(len(line) >= 2):
			#output the length of the hashtag and the untouched number of occurrences
			print str(len(line[0]) - 1) + '\t' + line[1] + '\n'
		
	
if __name__ == "__main__":
	main()
