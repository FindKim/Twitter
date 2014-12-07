#
#	Created by Kim Ngo, Nov. 18, 2014
# Assisted by Ryan Boccabella
#	Final Project
#	Cloud Computing - CSE40822
#
# Histogram of hashtags from tweets across time
#

clear
reset

set terminal postscript
set output "sample_plot_2.ps"

set title "Hashtag Lifetime"

set xtics rotate nomirror out
set ytics nomirror out
set auto x
set auto y
set xlabel "Time"
set ylabel "# of hashtag occurences"

set datafile separator "\t"

plot 'output_putin.txt' using 1:2

#pause -1
