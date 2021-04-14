

import csv
# import nltk

comments = []
with open('results.csv', 'r', encoding="utf-16") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row[1])
