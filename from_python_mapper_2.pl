#!/usr/bin/perl

while(<STDIN>)
{
	chomp();
	($tag, $count) = split();
	print "$count\t$tag\n";
}
