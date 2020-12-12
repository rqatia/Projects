#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix


# In[2]:


labels = pd.read_csv('labels.csv')


# In[3]:


labels.head(5)


# In[4]:


radiologist_accuracy = sum(labels.perfect_labeler == labels.radiologist)/len(labels)


# In[5]:


radiologist_accuracy


# In[6]:


confusion_matrix(labels.perfect_labeler.values,labels.radiologist.values,labels=["cancer","benign"])


# In[8]:


## Here, I'm going to change my entire dataframe to 0's and 1's to make processing easier
labels = labels.replace('cancer',1).replace('benign',0)
labels.head(7)


# In[9]:


algorithm_thresh = (labels.algorithm > 0.5)


# In[10]:


confusion_matrix(labels.perfect_labeler.values,algorithm_thresh,labels=[1,0])


# In[11]:


algorithm_thresh = (labels.algorithm > 0.4)
confusion_matrix(labels.perfect_labeler.values,algorithm_thresh,labels=[1,0])


# In[12]:


algorithm_thresh = (labels.algorithm > 0.6)
confusion_matrix(labels.perfect_labeler.values,algorithm_thresh,labels=[1,0])


# In[13]:


algorithm_thresh = (labels.algorithm > 0.5)
confusion_matrix(labels.radiologist.values,algorithm_thresh,labels=[1,0])

