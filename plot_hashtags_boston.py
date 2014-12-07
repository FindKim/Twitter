#!/usr/bin/python

import os
import sys

HASHTAG, TOTAL_COUNT = range(2)
HASHTAG, TIMESTAMP, COUNT = range(3)

def main():
	if (len(sys.argv) != 3):
		print 'Usage: ', sys.argv[0], ' [hashtag time stamp file] [hashtag total count file]\n'
		sys.exit(0)
	
	with open(sys.argv[2], 'r') as ht_count_file:
		top10_raw = [next(ht_count_file) for x in xrange(10)]

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
	
	for key in top10.keys():
		fname = 'output_' + key.strip('#') + '.txt'
		with open(fname, 'w') as f:
			for x in top10[key]:
				line = str(x[0]).replace(" ","") + '\t'+ str(x[1]) + '\n'
				f.write(line)
	
	os.system('gnuplot ./plot_hashtags_boston.gp')
	
	
	


#os.system("gnuplot plot_len_min_sum.gp")
#os.system("ps2pdf results/smallest_min_sum_p.001.ps results/smallest_min_sum_p.001.pdf")

if __name__ == "__main__":
	main()
