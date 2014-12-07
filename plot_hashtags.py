#!/usr/bin/python

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle

#script to take files from rounds 1 and 3 of mapreduce and prepare them
#for gnuplot graphing of the top n files. Writes output_#.txt files for
#use by plot_hashtags_sample.gp and calls plot_hashtags_sample.gp
#As an aside: plot_hashtags_sample.gp contains only 1 output_#.txt to graph, and this
#can be changed manually to see a different graph output in that .gp file

import os
import sys

HASHTAG, TOTAL_COUNT = range(2)
HASHTAG, TIMESTAMP, COUNT = range(3)
n = 10

def main():
	if (len(sys.argv) != 3):
		print 'Usage: ', sys.argv[0], ' [hashtag time stamp file] [hashtag total count file]\n'
		sys.exit(0)
	
	with open(sys.argv[2], 'r') as ht_count_file:
		top10_raw = [next(ht_count_file) for x in xrange(n)]

	# hashtag\ttotalcount
	top10_count = dict()	# (hashtag, total count)
	top10 = dict()	# (hashtag, list(pair(ts, count)))
	for line in top10_raw:
		line = line.strip()
		line = line.split('\t')
		top10_count[line[HASHTAG]] = int(line[TOTAL_COUNT])
		top10[line[HASHTAG]] = list()
	
	# hashtag\ttimestamp\tcount
	with open(sys.argv[1], 'r') as ht_ts_file:
		for line in ht_ts_file:
			line = line.strip()
			line = line.split('\t')
			ht = line[HASHTAG]
			
			if ht in top10_count.keys():
				top10[ht].append((line[TIMESTAMP], line[COUNT]))
	
	#write output files for easy graphing
	for key in top10.keys():
		fname = 'output_' + key.strip('#') + '.txt'
		with open(fname, 'w') as f:
			for x in top10[key]:
				line = str(x[0]).replace(" ","") + '\t'+ str(x[1]) + '\n'
				f.write(line)
	
	os.system('gnuplot ./plot_hashtags_sample.gp')

if __name__ == "__main__":
	main()
