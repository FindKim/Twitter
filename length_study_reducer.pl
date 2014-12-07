#!/usr/bin/perl

#Kim Ngo and Ryan Boccabella
#Cloud Computing Final Project - Hashtag Lifecycle Analysis

#The final stage of our final map reduce stage. This judges how hashtags of 
#different lengths hold up on average by accumulating the number of occurrences
#a hashtag of length X was tweeted and dividing by the number of unique hashtags
#of length X. For example #right\t5    #wrong\t13    #okay\t6 would output
#5\t9  and 4\t6 because right and wrong are both 5 letters long, there are 13 + 5 = 18
#occurrences of hashtags of length 5, and there are 2 unique hashtags.
#This will give an idea about the length of a trending hashtags, as trending tags pull
#up the calculated average.

$numOfLengthX = 0;
$totalCount = 0;
while(<STDIN>)
{
	chomp();
	($length, $occurrences) = 	split('\t');
	if(!defined($oldLength))
	{#define the first length, there has been 1 hastag of
	 #this length (numOfLengthX++) and it occurred occurrences times
		$oldLength = $length;
		$totalCount = $occurrences;
		$numOfLengthX++;
	}	 
	else
	{#everything but the first line
		if($oldLength eq $length)
		{#keep tallying for this length of hashtag
			$totalCount += $occurrences;
			$numOfLengthX++;
		}
		else
		{#length changed, print out info about the previous length
			if($numOfLengthX != 0)
			{
				$avg = (1.0 * $totalCount) / $numOfLengthX;
				print $oldLength."\t".$avg."\n";
			}
			
			#for the new hashtag length
			$oldLength = $length;
			$numOfLengthX = 1;
			$totalCount = $occurrences;
		}
	}
}

if($numOfLengthX != 0)
{
	$avg = (1.0 * $totalCount) / $numOfLengthX;
	print $oldLength."\t".$avg."\n";
}
	
