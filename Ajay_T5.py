#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[54]:


df = pd.read_csv("P:\\Prakash\\v\\model_data2.csv")


# In[55]:


df.head()


# In[56]:


df.shape


# In[58]:


df = df.dropna()


# In[59]:


df.shape


# In[60]:


drop = ['COWNNUM',
 'Count_product',
 'Age_Product1']


# In[61]:


df1 = df.drop(drop,1)


# In[62]:


df1.head()


# In[63]:


df1 = pd.get_dummies(df1.iloc[:,:-1])
df1.head()


# In[64]:


from scipy.spatial.distance import euclidean


# In[65]:


df1.tail()


# In[66]:


test = df1.tail(1)
# df = df[:-1]


# In[67]:


df1.tail(1)


# In[68]:


# dist = []
# for x in range(df.shape[0]):
#     dist.append(euclidean(test,df.iloc[x]))
# df["distances"] = dist


# In[69]:


for x in list(df1):
    df1[x] = df1[x].astype(float)


# In[70]:


dist = []
for x in range(df1.shape[0]):
    dist.append(euclidean(test,df1.iloc[x]))
df1["distances"] = dist


# In[46]:


df1.head()


# In[71]:


ind =list(df1.sort_values(by=['distances']).head(5).index)


# In[73]:


ind   ## the first element in the list is same as the test case so delete it.


# In[74]:


del ind[0]
ind


# In[77]:


most_closest_rows = df[df1.index.isin(ind)]


# In[78]:


most_closest_rows["Product_2"]


# In[80]:


ind1 = list(df1.sort_values(by=['distances']).head(100).index)


# In[81]:


ind1


# In[82]:


most_closest_rows1 = df[df.index.isin(ind1)]


# In[83]:


most_closest_rows1["Product_2"].value_counts()


# In[ ]:




