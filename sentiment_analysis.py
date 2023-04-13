import pandas as pd
from textblob import TextBlob
from google.colab import files
files.upload()

data = pd.read_csv('all stories - race.csv')

c = 0
all_sentiments = []
for i in range(len(data.index)):
	story = data['ENTIRE_STORY'][i]
	if type(data['ENTIRE_STORY'][i]) != float:
		test = data['ENTIRE_STORY'][i]
		blob = TextBlob(test)
		sentiment = blob.sentiment.polarity
		all_sentiments.append(sentiment)

a=len(all_sentiments)
c=0
for senti in all_sentiments:
  if senti > 0:
    c+=1
print('h',c)
import matplotlib.pyplot as plt
plt.boxplot(all_sentiments)
left, right = plt.xlim()
plt.hlines(0, xmin=left, xmax=right,  linestyles='--')
plt.show()

