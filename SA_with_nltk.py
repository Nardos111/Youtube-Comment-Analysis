

import csv
import nltk
import text2emotion as te
from nltk.sentiment import SentimentIntensityAnalyzer


comments = []
with open('results.csv', 'r', encoding="utf-16") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row[1])
combined_comments = ' '.join(comments)
word: list[str] = nltk.word_tokenize(combined_comments)
stopwords = nltk.corpus.stopwords.words("english")
words = [w for w in word if w.lower() not in stopwords and w.isalpha()
         and len(w) > 2]
fd = nltk.FreqDist(words)  # frequent words used
sa = SentimentIntensityAnalyzer()
print(sa.polarity_scores(combined_comments))
print(fd.most_common(10))
print(te.get_emotion(combined_comments))
