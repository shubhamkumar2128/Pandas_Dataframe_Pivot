#!/usr/bin/env python
# coding: utf-8

# In[127]:


import pandas as pd
df=pd.read_csv('C:\\ectbcsv.csv')
print(df)


# In[128]:


#Change pivot
tdf=df.pivot(index="date",columns="city")
print(tdf)


# In[129]:


#specific column
tdf=df.pivot(index="date",columns="city",values="humidity")
print(tdf)


# In[130]:


#avg of df entires
tdf=df.pivot_table(index="city",columns="date")
print(tdf)


# In[131]:


tdf=df.pivot_table(index="city",columns="date",aggfunc="sum")
print(tdf)


# In[132]:


#avg of each row & col value in All field
tdf=df.pivot_table(index="city",columns="date",margins=True)
print(tdf)


# In[133]:


df=pd.read_csv('C:\\ectbcsv2.csv')
print(df)


# In[138]:


#avg temperature of city b/w two different dates
df["date"]=pd.to_datetime(df["date"])
d=df.pivot_table(index=pd.Grouper(freq="M",key="date"),columns="city")
print(d)

