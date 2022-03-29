#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "the little white dog barked at the cat"
#Define your grammar using regular expressions
grammar = ('''NP: {<DT>?<JJ>*<NN>} # NP''')
chunkParser = nltk.RegexpParser(grammar)
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
print(tagged)

