## MLP Dataset Properties

1. How big is the dataset?
    The dataset has 36860 rows and 4 columns.

    ```
    # Rows
    wc -l clean_dialog.csv # alternative command

    # Columns
    head -1 clean_dialog.csv # "title","writer","pony","dialog"
    csvcut -n clean_dialog.csv # alternative command
    ```

2. What's the structure of the data?
    The columns are "title","writer","pony", and "dialog". The type of data in each field is a string/text value. This information was summarized using the following command:

    ```
    csvstat clean_dialog.csv
    ```

3. How many episodes does it cover?
    Each episode in the dataset has a unique title. From the previous command, `csvstat clean_dialog.csv`, we can see that there are 197 unique titles. This means that the dataset covers 197 episodes. There are no null values in this column, so we do not need to worry about missing data.

4. During the exploration phase, find at least one aspect of the dataset that is unexpected - meaning that it seems like it could create issues for later analysis.
    In the pony column, some data includes values such as 'Main cast sans [pony]', 'Main cast but [pony]', and 'Main cast except [pony]'. If looking at speaker frequency, this may cause issues in later analysis as they represent the same information but are presented differently. Additional care must be taken to account for them.

## Speaker Frequency
The steps below detail how I extracted speaker frequency. Looking at only the pony and dialog columns, rows where the dialog is `NA` were removed.

```
# Isolating pony and dialog columns
csvcut -c pony,dialog clean_dialog.csv > dialog.csv

# Removing rows with NA
grep -v NA$ dialog.csv > dialog.na_gone.csv
```
Each row represents one line of dialog. I am approximating each row to represent a single spoken line, therefore, only the `Pony` column is needed. The `Pony` column was extracted and sorted by frequency. To simplify the analysis, I am also assuming counting dialog for which the pony 

```
# Extracting pony column
csvcut -c pony dialog.na_gone.csv > pony.csv

# Calculating frequency
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
```
