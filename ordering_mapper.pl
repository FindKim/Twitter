#!/usr/bin/perl

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#This takes the output of the second round of map reduce (which outputted hashtag, wordcout
#pairs, and sets the pairs up to be sorted by the shuffle sorter so we can get them into descending
#order in a single file (that is:  most_common_hashtag\toccurrences\nsecond_most_common_hashtag\t
#occurrences ... least_common_hashtag\toccurrences).

while(<STDIN>)
{
	chomp();
	($tag, $count) = split();
	print "$count\t$tag\n";
}
