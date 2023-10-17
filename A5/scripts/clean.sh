#!/bin/bash

input=$1
file=$(basename $input .csv)
path=$(dirname $input)

# Extracting relevant columns
csvtool col 2,3,6,7,8,20 $path/$file.csv > $path/${file}_filtered.csv

# Creating csv with headers
cat $path/columns.txt > $path/${file}_filtered_columns.csv
cat $path/${file}_filtered.csv >> $path/${file}_filtered_columns.csv

# Filtering for 2020
csvgrep -c 1 -r "[01]./[01]./2020" $path/${file}_filtered_columns.csv > $path/${file}_2020.csv

# Remove data with no borough or missing data (will remove all open and in progress cases)
grep -ve Unspecified -ve ",," $path/${file}_2020.csv > $path/${file}_2020_filtered.csv
