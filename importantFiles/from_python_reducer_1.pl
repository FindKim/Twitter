#!/usr/bin/perl

$totalCount = 0;

while(<STDIN>)
{
	chomp();
	($tag, $singleCount) = split("\t");  #split based on tabs
	
	if(!defined($oldtag))
	{
		$oldtag = $tag;
	}
	else
	{
		if($oldtag eq $tag)
		{
			$totalCount += $singleCount;	
		}
		else
		{
			print $oldtag."\t".$totalCount."\n";
			$oldtag = $newtag;
			$totalCount = $singleCount;
		}
	}
}

print $oldtag."\t".$totalCount."\n";
