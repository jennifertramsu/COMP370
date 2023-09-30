import argparse

parser = argparse.ArgumentParser(
    prog="BoroughComplaints",
    description="This program outputs the number of complaint types per borough for a given date range.")

parser.add_argument("-i", "--input")
parser.add_argument("-s", "--start")
parser.add_argument("-e", "--end")
parser.add_argument("-o", "--output")

args = parser.parse_args()
