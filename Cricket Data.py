#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas
import pandas as pd


# In[2]:


# import csv
df = pd.read_csv('CricketData.csv')


# In[3]:


df


# In[4]:


# rename multiple columns in a list
df = df.rename(columns = {'Mat':'Matches','NO': 'Not_Outs', 'HS':'Highest_Inns_Score', 'BF':'Balls_Faced', 'SR':'Batting_Strike_Rate'})


# In[5]:


df


# In[6]:


#shows if there are nulls
df.isnull().any()


# In[8]:


#show specific
df[df['Balls_Faced'].isna() == 1]


# In[9]:


#replace with 0
df['Balls_Faced'] = df['Balls_Faced'].fillna(0)


# In[10]:


df['Batting_Strike_Rate'] = df['Batting_Strike_Rate'].fillna(0)


# In[14]:


df[df['Player'] == 'Hon.FS Jackson (ENG)' ]


# In[15]:


#Drop Duplicates
df.duplicated()


# In[16]:


df[df['Player'].duplicated() == 1]


# In[17]:


#show all
df[df['Player'].isin(['RG Pollock (SA)','GS Sobers (WI)','JB Hobbs (ENG)','TT Samaraweera (SL)'])]


# In[18]:


# automaticaly drops duplicates
df = df.drop_duplicates()


# In[20]:


df[df['Player'].isin(['RG Pollock (SA)','GS Sobers (WI)','JB Hobbs (ENG)','TT Samaraweera (SL)'])]


# In[21]:


# Split up Span into Start and End Date
df['Span'].str.split(pat = '-')


# In[22]:


#new column with first season of each
df['Rookie_Year'] = df['Span'].str.split(pat = '-').str[0]


# In[23]:


#new column with last season of each
df['Final_Year'] = df['Span'].str.split(pat = '-').str[1]


# In[24]:


df


# In[25]:


# drop span columns
df = df.drop(['Span'], axis = 1)


# In[27]:


df.head()


# In[28]:


# split the country from the player
df['Player'].str.split(pat = '(')


# In[29]:


df['Country'] = df['Player'].str.split(pat = '(').str[1]


# In[30]:


df['Country'] = df['Country'].str.split(pat = ')').str[0]


# In[31]:


df['Country']


# In[32]:


# lets fix the player
df['Player'] = df['Player'].str.split(pat = '(').str[0]


# In[33]:


df.head()


# In[34]:


# change data types
df.dtypes


# In[35]:


#first remove astheriscs
df['Highest_Inns_Score'] = df['Highest_Inns_Score'].str.split(pat = '*').str[0]


# In[37]:


#turn to int
df['Highest_Inns_Score'] = df['Highest_Inns_Score'].astype('int')


# In[38]:


df.dtypes


# In[39]:


df = df.astype({'Rookie_Year':'int','Final_Year':'int'})


# In[41]:


df['Matches'] = df['Matches'].astype('int')


# In[43]:


df['Balls_Faced'] = df['Balls_Faced'].str.split(pat = '+').str[0]


# In[45]:


df['Balls_Faced'] = df['Balls_Faced'].fillna(0)
df['Balls_Faced'] = df['Balls_Faced'].astype('int')
df[df['Balls_Faced'].isna() == 1]


# In[47]:


df.dtypes


# In[48]:


# Build up a career length column
df['Career_Length'] = df['Final_Year'] - df['Rookie_Year']


# In[49]:


#quiestion 1. ehat is the average career length?
df['Career_Length'].mean()


# In[52]:


#auestion 2. AVG batting_strike_rate for players who played over 10 years
df[df['Career_Length']> 10]['Batting_Strike_Rate'].mean()


# In[53]:


#question3. find number of cricketers who played before 1960
df[df['Rookie_Year']<1960]['Player'].count()


# In[56]:


# question 4. max highest inns score by country
df.groupby('Country')['Highest_Inns_Score'].max().to_frame('Highinncountry').reset_index().sort_values('Highinncountry', ascending = False)


# In[58]:


#question 5. Hundreds, Fifties, ducks (0) AVG by Country
df.groupby('Country')[['100','50','0']].mean()


# In[ ]:




