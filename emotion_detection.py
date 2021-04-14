import io
import csv

with open('results.csv', 'r', encoding="utf-16") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
