# COMP370 Intro to Data Science

## Mini-Project 1
### Description

In this assignment, you will conduct an analysis of tweets produced by Russian trolls during the 2016 US election.  These tweets were published by 538.

In this mini-project, we’ll be assessing the frequency with which troll tweets mention “Trump” by name.

<ul> 
1.	Data Collection

<ul> 
a.	Download the raw tweet data.  You will ONLY be using the data from the first file (IRAhandle_tweets_1.csv).

b.	Looking at only the first 10,000 tweets in the file, keep those that (1) are in English and (2) don’t contain a question.  This will be our dataset.  To filter the right tweets out, take a look at the columns. 
    
<ul> 
i.	There are specific columns that call our language.  You can trust these.

ii.	Assume that a tweet which contains a question contains a “?” character. </ul>

c.	Create a new file (I would suggest in TSV – tab-separated-value - format) containing these tweets.
</ul>
</ul>

<ul>
2.	Data Annotation

<ul> 
a.	To do our analysis, we need to add one new feature: whether or not the tweet mentioned Trump. This feature “trump_mention” is Boolean (=”T”/”F”).  A tweet mentions Trump if and only if it contains the word “Trump” (case-sensitive) as a word.  This means that it is separated from other alphanumeric letters by either whitespace OR non-alphanumeric characters (e.g., “anti-Trump protesters” contains “trump”, but “I got trumped” does not).
    
b.	Create a new version of your dataset that contains this additional feature.
</ul></ul>

<ul>
3.	Analysis

<ul>
a.	Using your newly annotated dataset, compute the statistic: % of tweets that mention Trump.

b.	It turns out that our approach isn’t counting tweets properly … meaning that some tweets are getting counted more than once.  Go through and look at your annotated data.  Identify where the counting problem is coming from.

</ul>
</ul>

## Homework 2
### Description

The goal of this assignment is for you to get more familiar with your Unix EC2 – both as a data science machine and as a server (as a data scientist, you’ll need it as both).

<ul>
1. Setting up a webserver

<ul>
a. Setup an EC2 instance to run an Apache webserver on port 8008.

b. Your goal is to have it serving up the file comp370_hw2.txt at the www root.
</ul>

2. Setting up a database server
<ul>
a. Install the MariaDB database server on your EC2 instance.

b. Configure the database to run on an external port.

c. Create a database called “comp370_test”.

d. Add a new user "comp370" to your database server with permission to access the database "comp370_test". Use the password "$ungl@ss3s" for the password for this user.
</ul>
</ul>

## Homework 3
### Description

The goal of this assignment is to use UNIX command line tools to do core data science work.

<ul>
1. Watch some My Little Pony episodes (totally optional)
<ul>
In this and the next homework, we’re going to be analyzing My Little Pony language.  As we’ve discussed, it’s always important to study your source material … particularly when it’s very entertaining cartoons!  So if you’re able, watch a couple episodes!
</ul>
2. Explore MLP Dataset Properties
<ul>
We’ll be using the dataset available (here)[https://www.kaggle.com/liury123/my-little-pony-transcript]

For the purpose of this study, we’ll use only clean_dialog.csv and assume that the dataset is perfect.

Using standard command line tools (e.g., head, more, grep) and csvtool (shown in the solution to HW1), explore the clean_dialog.csv. Use the command line tools to answer the following questions:
-	How big is the dataset?
-	What’s the structure of the data? (i.e., what are the field and what are values in them)
-	How many episodes does it cover?
-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.
</ul>
3. Analyze Speaker Frequency
<ul>
Use the grep tool to determine how often each pony speaks.
Now calculate the percent of lines that each pony has over the entire dataset (including all characters).
</ul>