#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


# In[2]:


txt = "Sukanya, Rajib and Naba are my good friends. "     "Sukanya is getting married next year. "     "Marriage is a big step in one’s life."     "It is both exciting and frightening. "     "But friendship is a sacred bond between people."     "It is a special kind of love between us. "     "Many of you must have tried searching for a friend "    "but never found the right one."


# In[3]:


tokenized = sent_tokenize(txt)
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words] 
    tagged = nltk.pos_tag(wordsList)
    print(tagged)

