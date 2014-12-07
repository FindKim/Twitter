#!/usr/bin/perl

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#This is the second part of the assisted word count like MapReduce which
#keeps an accumulator for each hashtag that comes in and then prints out 
#that tag and its total count. It is the reducer in the second round of
#our MapReduce on the way to a descending order file

$totalCount = 0;

while(<STDIN>)
{
	chomp();
	($tag, $singleCount) = split("\t");  #split based on tabs
	
	if(!defined($oldtag))
	{#if there is no tag yet, define it for easy switching
	 #and set the total count equal to the singlecount of
	 #of the first line
		$oldtag = $tag;
		$totalCount += $singleCount
	}
	else
	{
		if($oldtag eq $tag)
		{#if we're still on the same tag...
			$totalCount += $singleCount;	
		}
		else
		{#if we've changed tags, output results and get ready
		 #for a new one
			print $oldtag."\t".$totalCount."\n";
			$oldtag = $newtag;
			$totalCount = $singleCount;
		}
	}
}

#print the last of the tags
print $oldtag."\t".$totalCount."\n";
