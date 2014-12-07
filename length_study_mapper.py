#!/usr/bin/python

import fileinput
import sys
import string

def main():
	if(len(sys.argv) != 3):
		print 'Usage: ', sys.argv[0], ' [hashtags total count file] [top n hashtags]\n'
		sys.exit(0)
	
	with open(sys.argv[2], 'r') as ht_count_file:
		top_n_raw = [next(ht_count_file) for x in xrange(int(sys.argv[1]))]
		
	for line in top_n_raw:
		line = line.strip()
		line = line.split('\t')
		if(len(line) >= 2):
			print str(len(line[0]) - 1) + '\t' + line[1] + '\n'
		
	
if __name__ == "__main__":
	main()
