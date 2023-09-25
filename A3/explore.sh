#!/bin/bash

ponies=("Twilight Sparkle" "Applejack" "Fluttershy" "Pinkie Pie" "Rainbow Dash" "Rarity")
total=$(csvtool height pony.csv)
counts=(0 0 0 0 0 0)

for i in {0..5}
do
    pony=${ponies[i]}

    echo $pony
    ind_count=$(grep "$pony" pony.csv | wc -l)
    echo "Individual count: $ind_count"

    exception=$(grep -e "sans.* $pony" -e "except.* $pony" -e "but.* $pony" pony.csv | wc -l)
    echo "Exception count: $exception"

    exception=`echo "$exception * 2" | bc` # Remove double counting
    
    cast=$(grep "Main cast" pony.csv | wc -l)
    echo "Cast count: $cast"

    count=`expr $ind_count - $exception + $cast`

    echo $count
    counts[i]=$count

    echo
done

echo ${counts[@]}

freqs=(0 0 0 0 0 0)

for i in {0..5}
do
    count=${counts[i]}
    freq=`printf %.2f $(echo "($count / $total) * 100" | bc -l)`
    freqs[i]=$freq
done

echo ${freqs[@]}

# Constructing CSV file
echo "pony_name", "total_line_count", "percent_all_lines" > line_percentages.csv

for i in {0..5}
do
    echo ${ponies[i]}, ${counts[i]}, ${freqs[i]} >> line_percentages.csv
done