import argparse
import pandas as pd
from pathlib import Path

# Creating ArgumentParser
parser = argparse.ArgumentParser(
    prog="AverageResponseTime",
    description="This program calculates the monthly average response time for a given category.")

parser.add_argument("-i", "--input")
parser.add_argument("-c", "--category")
parser.add_argument("-o", "--output")

args = parser.parse_args()

# Assigning variables
input = args.input
category = args.category
output = args.output

if input == None:
    print("Please specify an input file.")
    exit(1)
if category == None:
    print("Please specify a category.")
    exit(1)

# Reading in data
df = pd.read_csv(input).loc[:, ['closed date', 'complaint type', 'incident zip', 'create-to-closed time']]
df['closed date'] = pd.to_datetime(df['closed date'], format='%Y-%m-%d %H:%M:%S')
df['month'] = df['closed date'].dt.month

# Groupby category and month
df_filtered = df[[category, 'month', 'create-to-closed time']]
df_avg = df.groupby([category, 'month'])['create-to-closed time'].mean().reset_index().rename(columns={'create-to-closed time': 'avg response time'})

# Mapping month to month name
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
          6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
          11: 'November', 12: 'December'}

df_avg['month'] = df_avg['month'].map(months)

if output == None:
    print(df_avg)
else:
    df_avg.to_csv(output, index=False)