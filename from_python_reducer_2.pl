#!/usr/bin/perl

while(<STDIN>)
{
	chomp();
	($total, $tag) = split("\t");
	print $tag."\t".$total."\n";
}
