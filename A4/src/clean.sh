#!/bin/bash

path=../data
file=$path/nyc_311_limit

# # Extracting relevant columns
# csvtool col 2-4,6,9,20,26 $file.csv > $path/${file}_filtered.csv

# # Creating csv with headers
# cat $path/columns.txt > $path/${file}_filtered_columns.csv
# cat $path/${file}_filtered.csv >> $path/${file}_filtered_columns.csv

# # Filtering for 2020
# csvgrep -c 1 -r "[01].\/[01]./2020" $path/${file}_filtered_columns.csv > $path/${file}_2020.csv

# Remove data with no borough or missing data
grep -ve Unspecified -ve ",," $path/${file}_2020.csv > $path/${file}_2020_filtered.csv
