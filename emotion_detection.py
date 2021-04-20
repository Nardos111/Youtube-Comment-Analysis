# Sentiment analysis

import io
import csv
from textblob import TextBlob


def posaneg():
    comments = []
    with open('results.csv', 'r', encoding="utf-16") as file:
        reader = csv.reader(file)
        for row in reader:
            comments.append(row[1])
    if "Username" in comments:
        comments.remove("Username")
    if "Comment" in comments:
        comments.remove("Comment")
    positive_comments = []
    negative_comments = []

    for comment in comments:
        comment_polarity = TextBlob(comment).sentiment.polarity
        if comment_polarity > 0:
            positive_comments.append(comment)
        else:
            negative_comments.append(comment)
    with io.open('comment_class.csv', 'w', newline='', encoding="utf-16") as file:
        writer = csv.writer(file)
        writer.writerow(positive_comments)
        writer.writerow(negative_comments)
    return


posaneg()
