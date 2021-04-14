# Sentiment analysis

import io
import csv
from textblob import TextBlob

comments = []
with open('results.csv', 'r', encoding="utf-16") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row[1])
positive_comments = []
negative_comments = []

for comment in comments:
    comment_polarity = TextBlob(comment).sentiment.polarity
    if comment_polarity > 0:
        positive_comments.append(comment)
    else:
        negative_comments.append(comment)


print('Positive comment count: {}'.format(len(positive_comments)))
print(positive_comments)
print('Negative comment count: {}'.format(len(negative_comments)))
print(negative_comments)
