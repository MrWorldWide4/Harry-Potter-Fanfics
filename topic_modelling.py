# -*- coding: utf-8 -*-
"""topic modelling - race.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BCRFEIkZdOA0hnQiBAwtBkBjmKb0ebnK
"""

!pip install top2vec
# !pip uninstall numpy
# !pip install numpy==1.22
import pandas as pd
import nltk
from top2vec import Top2Vec

from google.colab import files
files.upload()

nltk.download('words')
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
realwords = set(nltk.corpus.words.words())

data = pd.read_csv('all stories - race.csv')
all_stories = []
# all_stories = ['my name is hassan', 'hello i am called hassan']
for i in range(len(data.index)):
	story = data['ENTIRE_STORY'][i]
	if type(data['ENTIRE_STORY'][i]) != float:
		temp = " ".join(w for w in nltk.wordpunct_tokenize(story) \
         if w.lower() in realwords or not w.isalpha())
		temp = [word for word in temp.split() if word.lower() not in stopwords]
		temp = " ".join(temp)
		all_stories.append(temp)

all_stories = all_stories*3
print('data opened')
model = Top2Vec(all_stories)
print('model made')
topic_sizes, topic_nums = model.get_topic_sizes()
print('topic sizes: ' , topic_sizes)
print('topic nums: ' , topic_nums)

topic_words, word_scores, topic_nums = model.get_topics()
listofdictionaries = []
for words, scores, num in zip(topic_words, word_scores, topic_nums):
	res = dict(zip(words, scores))
	listofdictionaries.append(res)
	# print(num)
	# print(words)
	# print(f"Words: {words}")	
	# print(f"Words: {scores}")
print(listofdictionaries)

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

wc = WordCloud(background_color="white",width=1500,height=1500, max_words=50,relative_scaling=0.9,normalize_plurals=False).generate_from_frequencies(listofdictionaries[4])
plt.imshow(wc)