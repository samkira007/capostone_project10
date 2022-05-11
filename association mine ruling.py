#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori


# In[35]:


store_data = pd.read_csv('store_data (1).csv')
store_data.head()


# In[51]:


store_data = pd.read_csv('store_data (1).csv', header=None)
store_data.head()


# In[52]:


records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])


# In[57]:


association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)


# In[58]:


print(association_results)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




