#!/usr/bin/perl

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
