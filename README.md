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