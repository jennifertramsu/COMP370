import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime

# Creating ArgumentParser
parser = argparse.ArgumentParser(
    prog="BoroughComplaints",
    description="This program outputs the number of complaint types per borough for a given date range. It also removes rows where the closed date is before the created date and calculated the response time in hours. This new dataframe is exported as a csv file.")

parser.add_argument("-i", "--input")
parser.add_argument("-s", "--start", default="01/01/2020")
parser.add_argument("-e", "--end", default="12/31/2020")
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

# Reading in data, status is already closed for all rows due to pre-processing and trimming
df = pd.read_csv(input).loc[:, ['created date', 'closed date', 'incident zip', 'complaint type', 'borough']]

# Filtering out rows where closed date is before created date
df['created date'] = pd.to_datetime(df['created date'], format='%m/%d/%Y %I:%M:%S %p')
df['closed date'] = pd.to_datetime(df['closed date'], format='%m/%d/%Y %I:%M:%S %p')
df_timefiltered = df[df['created date'] < df['closed date']]

# Calculate create-to-closed time in hours
timedelta = df_timefiltered['closed date'] - df_timefiltered['created date']
df_timefiltered['create-to-closed time'] = timedelta.apply(lambda x: x.round(freq='H')) / pd.Timedelta('1 hour')

# Export
df_timefiltered.to_csv("../data/" + Path(input).stem + "_ordered.csv", index=False)

# Filtering rows within given date range
df_range = df_timefiltered.loc[(df_timefiltered['created date'] >= start) & (df_timefiltered['created date'] <= end)]

# Organizing by complaint type and borough
df_complaints = df_range.loc[:, ['complaint type', 'borough']]
complaints = df_range.groupby(['complaint type', 'borough'], as_index=False).size().rename(columns={'size': 'count'})

if output != None:
    complaints.to_csv(output, index=False)
else:
    print(complaints)