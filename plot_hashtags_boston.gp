#
#	Created by Kim Ngo, Nov. 18, 2014
#	Final Project
#	Cloud Computing - CSE40822
#
# Histogram of hashtags from tweets across time
#

clear
reset

set terminal postscript
set output "sample_plot_boston.ps"

set title "Hashtag Lifetime"

set xtics rotate nomirror out
set ytics nomirror out
set auto x
set auto y
set xlabel "Time"
set ylabel "# of hashtag occurences"

set datafile separator "\t"

plot 'output_bostonmarahton.txt' using 1:2

#pause -1
