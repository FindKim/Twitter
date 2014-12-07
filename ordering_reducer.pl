#!/usr/bin/perl

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#The reducer in the third round of mapreduce which takes the sorted data
#in descending order (achieved by -nr on your output key comparator class)
#and swaps the key and the value so that the file written is hashtag first.
#input comes from ordering_mapper.pl

while(<STDIN>)
{
	chomp();
	($total, $tag) = split("\t");
	print $tag."\t".$total."\n";
}
