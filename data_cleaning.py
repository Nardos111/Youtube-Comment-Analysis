import re
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import spacy

df = pd.read_csv('output_scraping.csv', sep=',')
df.head()

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
df['new_comments'] = df['comments'].apply(
    lambda x: " ".join(x.lower() for x in x.split()))
df['new_comments'].head()
df['new_comments'] = df['new_comments'].str.replace('[^\w\s]', '', regex=True)
df['new_comments'].head()


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


df['new_comments'] = df['new_comments'].apply(lambda x: remove_emoji(x))
stop = stopwords.words('english')
df['new_comments'] = df['new_comments'].apply(
    lambda x: " ".join(x for x in x.split() if x not in stop))
df.head(20)


def space(comment):
    doc = nlp(comment)
    return " ".join([token.lemma_ for token in doc])


df['new_comments'] = df['new_comments'].apply(space)
df.head(20)

print(df['new_comments'])
