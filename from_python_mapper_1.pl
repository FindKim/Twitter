#!/usr/bin/perl

while(<STDIN>)
{
	chomp();
	($key, $timestamp, $count) = split("\t");  #split based on tabs
	print $key."\t".$count."\n";
}
