#!/usr/bin/perl

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
	{
		if($oldLength eq $length)
		{#keep tallying for this length of hashtag
			$totalCount += $occurrences;
			$numOfLengthX++;
		}
		else
		{#length changed, print out info about the previous length
			$avg = (1.0 * $totalCount) / $numOfLengthX;
			print $oldLength."\t".$avg."\n";
			
			#for the new hashtag length
			$oldLength = $length;
			$numOfLengthX = 1;
			$totalCount = $occurrences;
		}
	}
}

$avg = (1.0 * $totalCount) / $numOfLengthX;
print $oldLength."\t".$avg."\n";
	
	
