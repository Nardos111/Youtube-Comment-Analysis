import csv
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def generatewc():
    cdict = {}
    with open('cleandata.csv', 'rt', encoding="UTF-8") as f:
        reader = csv.reader(f)
        for i in reader:
            if i[1] not in cdict and i[1].isdigit():
                cdict[i[1]] = []
            if i[1] in cdict:
                cdict[i[1]].append(i[2])
        for k in cdict:
            cdict[k] = 't'.join(cdict[k])
        for k in cdict:
            wordcloud = WordCloud(max_font_size=40).generate(cdict[k])
            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.savefig("./static/%splot.jpg" % str(int(k)+1))
        return "OK"
