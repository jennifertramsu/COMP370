#!/bin/bash

csvtool height clean_dialog.csv # 36860 rows
wc -l clean_dialog.csv 
head -1 clean_dialog.csv # "title","writer","pony","dialog"