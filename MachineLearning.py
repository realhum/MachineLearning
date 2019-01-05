#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re 
import codecs
import numpy as np


# In[2]:


file_obj = codecs.open('news_train.txt', 'r', "utf-8")


# In[3]:


strings = []
for line in file_obj:
    strings.append(line.strip().lower())


# In[4]:


len(strings)


# In[5]:


print strings[0]


# In[6]:


type_list = []
text_list = []
for i in range(len(strings)):
    temp = strings[i].split("\t")
    text_list.append(temp[2])
    type_list.append(temp[0])


# In[7]:


print text_list[0]


# In[8]:


words = []
for i in range(len(text_list)):
    words.append(re.split(u'[^а-я]', text_list[i]))


# In[9]:


found = True
while(found):
    c = 0
    found = False
    for i in words:
        for j in i:
            if(j == ''):
                found = True
                words[c].remove('')
        c = c + 1


# In[10]:


type_dict = dict()
c = 0
for i in type_list:
    if(not(i in type_dict)):
        type_dict[i] = c
        c += 1
type_arr = []
c = 0
for i in type_list:
    if(not(i in type_dict)):
        type_arr.append
        c += 1


# In[11]:


words_dict = dict()
c = 0
for i in words:
    index_type = type_dict[type_list[c]]
    for j in i:
        if(not(j in words_dict) and (len(j)>=3)):
            words_dict[j] = np.zeros(10)
            words_dict[j][index_type] += 1
        elif(len(j)>=3):
            words_dict[j][index_type] +=1
    c += 1


# In[12]:


print type_dict


# In[13]:


for i in words:
    for j in i:
        sum = 0.0
        if(j in words_dict):
            for c in words_dict[j]:
                sum = sum + c
            words_dict[j] = np.true_divide(words_dict[j], sum)

print words_dict[u"когда"]
sum = 0
for i in words_dict[u"когда"]:
    sum = sum + i
print sum


# In[14]:


count = 0
c = 0
#while(score>=0.5):
for i in words:
    temp = np.zeros(10)
    for j in i:
        if(j in words_dict):
            temp = temp + words_dict[j]
    for type_art, index in type_dict.items():
        if (index == np.argmax(temp)):
            search = type_art
    if(search == type_list[c]):
        count += 1
    c += 1


# In[16]:


file_test = codecs.open('news_test.txt', 'r', "utf-8")


# In[17]:


strings = []
for line in file_test:
    strings.append(line.strip().lower())


# In[18]:


text_list = []
for i in range(len(strings)):
    temp = strings[i].split("\t")
    text_list.append(temp[1])


# In[19]:


words_test = []
for i in range(len(text_list)):
    words_test.append(re.split(u'[^а-я]', text_list[i]))


# In[20]:


found = True
while(found):
    c = 0
    found = False
    for i in words_test:
        for j in i:
            if(j == ''):
                found = True
                words_test[c].remove('')
        c = c + 1


# In[23]:


file_write = open('news_output.txt', 'w')
c = 0
for i in words_test:
    temp = np.zeros(10)
    check = False
    for j in i:
        if(j in words_dict):
            temp = temp + words_dict[j]
    for type_art, index in type_dict.items():
        if (index == np.argmax(temp)):
            file_write.write(type_art+'\n')
            check = True
    if(not check):
        file_write.write("forces\n")
    c += 1
file_write.close()

