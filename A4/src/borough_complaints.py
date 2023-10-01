import argparse
import pandas as pd
from datetime import datetime

# Creating ArgumentParser
parser = argparse.ArgumentParser(
    prog="BoroughComplaints",
    description="This program outputs the number of complaint types per borough for a given date range.")

parser.add_argument("-i", "--input")
parser.add_argument("-s", "--start")
parser.add_argument("-e", "--end")
parser.add_argument("-o", "--output")

args = parser.parse_args()

# Assigning variables
input = args.input
start = datetime.strptime(args.start, '%m/%d/%Y')
end = datetime.strptime(args.end, '%m/%d/%Y')
output = args.output

if input == None:
    print("Please specify an input file.")
    exit(1)
if start == None:
    print("Please specify a start date.")
    exit(1)
if end == None:
    print("Please specify an end date.")
    exit(1)

# Reading in data
df = pd.read_csv(input).loc[:, ['created date', 'closed date', 'complaint type', 'borough']]

# Filtering out rows where closed date is before created date
df.loc[:, ['created date', 'closed date']] = df.loc[:, ['created date', 'closed date']].apply(pd.to_datetime, format='%m/%d/%Y %I:%M:%S %p')
df_timefiltered = df.loc[df['created date'] < df['closed date']]

# Filtering rows within given date range
df_range = df_timefiltered.loc[(df_timefiltered['created date'] >= start) & (df_timefiltered['created date'] <= end)]

# Organizing by complaint type and borough
df_complaints = df_range.loc[:, ['complaint type', 'borough']]
complaints = df_range.groupby(['complaint type', 'borough'], as_index=False).size().rename(columns={'size': 'count'})

if output != None:
    complaints.to_csv(output, index=False)
else:
    print(complaints)