#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, pprint, string
import pandas as pd
from nltk import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.util import ngrams
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


# In[2]:


string.punctuation = string.punctuation +'“'+'”'+'-'+'’'+'‘'+'—'
string.punctuation = string.punctuation.replace('.', '')


# In[6]:


corpus = pd.read_csv('C:/Users/Admin/Downloads/corpus.csv')
print(corpus)
file_nl_removed = ""
for line in corpus:
  line_nl_removed = line.replace("\n", " ")      #removes newlines
  file_nl_removed += line_nl_removed
file_p = "".join([char for char in file_nl_removed if char not in string.punctuation])   #removes all special characters

print(file_p)


# In[7]:


sents = nltk.sent_tokenize(file_p)
print(sents)
print("The number of sentences is", len(sents)) 
#prints the number of sentences

words = nltk.word_tokenize(file_p)
print(words)
print("The number of tokens is", len(words)) 
#prints the number of tokens

average_tokens = round(len(words)/len(sents))
print("The average number of tokens per sentence is",average_tokens) 
#prints the average number of tokens per sentence

unique_tokens = set(words)
print("The number of unique tokens are", len(unique_tokens)) 
#prints the number of unique tokens


# In[8]:


unigram=[]
bigram=[]
trigram=[]
fourgram=[]
tokenized_text = []
for sentence in sents:
    sentence = sentence.lower()
    sequence = word_tokenize(sentence) 
    for word in sequence:
        if (word =='.'):
            sequence.remove(word) 
        else:
            unigram.append(word)
    tokenized_text.append(sequence) 
    bigram.extend(list(ngrams(sequence, 2)))  
#unigram, bigram, trigram, and fourgram models are created
    trigram.extend(list(ngrams(sequence, 3)))
    fourgram.extend(list(ngrams(sequence, 4)))


# In[9]:


def removal(x):     
#removes ngrams containing only stopwords
    y = []
    for pair in x:
        count = 0
        for word in pair:
            if word in stop_words:
                count = count or 0
            else:
                count = count or 1
        if (count==1):
            y.append(pair)
    return(y)


# In[10]:


bigram = removal(bigram)
trigram = removal(trigram)             
fourgram = removal(fourgram)
freq_bi = nltk.FreqDist(bigram)
freq_tri = nltk.FreqDist(trigram)
freq_four = nltk.FreqDist(fourgram)
print("Most common n-grams without stopword removal and without add-1 smoothing: \n")
print ("Most common bigrams: ", freq_bi.most_common(5))
print ("\nMost common trigrams: ", freq_tri.most_common(5))
print ("\nMost common fourgrams: ", freq_four.most_common(5))

