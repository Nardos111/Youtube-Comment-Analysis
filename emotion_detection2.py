import csv
import text2emotion as te

comments = []
with open('results.csv', 'r', encoding="utf-16") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row[1])
combined_comments = ' '.join(comments)
print(te.get_emotion(combined_comments))
# Add emotion percentage graph later
