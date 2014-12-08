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

# CHANGE OUTPUT FILE NAME
# COMMAND ps2pdf TO CONVERT PS TO PDF
set output "sample_plot_2.ps"

set title "Hashtag Lifecycle"

set xtics rotate nomirror out
set ytics nomirror out
set auto x
set auto y
set xlabel "Time"
set ylabel "# of hashtag occurences"

set datafile separator "\t"


# CHANGE INPUT FILE TO PLOT
plot 'output_putin.txt' using 1:2
