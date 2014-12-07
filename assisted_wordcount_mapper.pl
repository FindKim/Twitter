#!/usr/bin/perl

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#Takes information from first round of mapreduce with tweet_mapper_*.py
# and tweet_reducer.py, just takes advantage of the fact that some counting
# has already been done. This is the first (well, third since it's the second
# round of mapreduce) step of word count. Results go to assisted_wordcount_reducer.pl

while(<STDIN>)
{
	chomp();
	($key, $timestamp, $count) = split("\t");  #split based on tabs
	print $key."\t".$count."\n";
}
