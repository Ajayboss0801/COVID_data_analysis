#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import piplite
await piplite.install('seaborn')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("country_wise_latest.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.describe(include="O") ## for categorical columns


# In[9]:


df.shape


# In[ ]:





# ## **EDA**
# 
# ## TOP 5 COUNTIRES THAT GIVES MAX NO. OF CASES

# In[10]:


df.head()


# In[11]:


max_case = df[["Country/Region" , "Confirmed"]]
max_case


# In[12]:


max_case = max_case.sort_values(ascending=False , by = "Confirmed")[0:5]
max_case


# In[13]:


plt.pie (max_case["Confirmed"], labels = ["US", "Brazil" , "India", "Russia", "S Africa"] , autopct= "%0.2f%%" , shadow=True )
plt.title("Max_case_Countries")
plt.show()


# - According to above insight US Country gives the maximum number of covid cases
# 

# ## Top 10 countrys that has recorded max number of death cases

# In[14]:


df.head()


# In[15]:


max_Death = df[["Country/Region" , "Deaths"]]
max_Death


# In[16]:


max_Death = max_Death.sort_values(ascending = False , by = "Deaths" )[0:10]
max_Death


# In[17]:


plt.pie(max_Death["Deaths"], labels = ["ÜS","Brazil","UK","Mexico","Italty","India","France","Spain","Peru","Iran"], autopct = "%0.2f%%" , shadow = True)
plt.title("Max_Death_Countris")
plt.show()


# In[ ]:





# - According to above insight US Country has the maximum number of covid Deaths
# 

# ### percentage of recovery in respective states

# In[18]:


df.head()


# In[19]:


rec_df = df[["Country/Region" , "Recovered"]]
rec_df


# In[20]:


rec_df = rec_df.sort_values(ascending=False , by ="Recovered")[0:10]
rec_df


# In[21]:


plt.pie(rec_df["Recovered"] ,labels = rec_df["Country/Region"] , autopct="%0.2f%%" , shadow=True )
plt.title("Max_Recovered_Countries")
plt.show


# 
# - Brazil, US and India has the most recovered rate of covid case resp.
# 

# ## Which country faces the maximum number of death case

# In[22]:


df.head()


# In[23]:


max_death = df[["Country/Region" , "Deaths / 100 Cases"]]
max_death


# In[24]:


max_death = max_death.sort_values(ascending = False , by = "Deaths / 100 Cases")[0:10]
max_death


# In[25]:


x = np.array(max_death["Country/Region"])
y = np.array(max_death["Deaths / 100 Cases"])

sns.barplot(x=y , y=x )


# - Yemen country got the highest number of death per 100 cases

# ## which country experiences the maximum frequency of recovery case

# In[26]:


df.head()


# In[82]:


max_freq = df[["Country/Region" , "Recovered / 100 Cases"]]
max_freq


# In[85]:


max_freq = max_freq.sort_values(ascending = False , by="Recovered / 100 Cases" )[0:10]
max_freq


# In[88]:


x = np.array(max_freq["Country/Region"])
y = np.array(max_freq["Recovered / 100 Cases"])
             
sns.barplot(x = x , y = y)
plt.xticks(rotation=30)


# - According to above data Holy See country has the fastest recovery frequency

# ### WHO Region wise Data

# In[90]:


df.head()


# In[97]:


who_df = df[["Country/Region" ,"Confirmed last week" ,  "WHO Region"]]


# In[98]:


who_df


# In[100]:


who_df = who_df.sort_values(ascending = False , by = "Confirmed last week")[0:10]
who_df


# In[116]:


plt.pie(who_df["Confirmed last week"] , labels = (who_df["WHO Region"]) , autopct = "%0.2f%%" , shadow = True)
plt.legend(who_df["Country/Region"] , loc = "center")


# - Above data says that America's and South-east asis's  WHO Regionss are the top most regions where affect the maximum number of confirmed covid results.  

# ### maximum death, confirmed and recovery as per who region

# In[117]:


df.head()


# In[124]:


max_who = df[["Country/Region" , "Confirmed" , "Deaths" , "Recovered" , "WHO Region"]]
max_who


# In[131]:


max_con = max_who.sort_values(ascending = False , by= "Confirmed")[0:10]
max_con


# In[132]:


max_death = max_who.sort_values(ascending = False , by = "Deaths")[0:10]
max_death


# In[133]:


max_rec = max_who.sort_values(ascending = False , by = "Recovered")[0:10]
max_rec


# In[144]:


print("Maximum confirmed cases by WHO region")
print("\n")
print(max_con)
print("\n")
print("Maximum deaths reported by WHO region")
print("\n")
print(max_death)
print("\n")
print("Maximum numbers of cases recovered by WHO region")
print("\n")
print(max_rec)


# ### EDA 2

# ### As we know US is the most affected country due to covid, lets see its latitude & longitude.

# In[2]:


df1 = pd.read_csv("covid_19_clean_complete.csv")


# In[3]:


df1


# In[4]:


df1.head()


# In[5]:


df2 = df1[df1["Country/Region"] == "US"]
df2


# In[166]:


us_lat_lon = df2.iloc[0:1 , 1:4] ## df[["column1","column2","column3"][rows from:rows to]
us_lat_lon


# 

# ### India & Brazil are the countries with the highest recovery rate. lets see the latitude & longitude.

# In[187]:


df2 = df1[(df1["Country/Region"] == "India") | (df1["Country/Region"]=="Brazil")]
df2


# In[188]:


df2 = df2[["Country/Region","Lat","Long"]][0:2]
df2


# ### yamen has the hghets number of death per case frequency lets see its latitude & longitude

# In[198]:


df3 = df1[df1["Country/Region"]=="Yemen"]
df3


# In[200]:


df3 = df3.iloc[0:1 , 1:4]
df3


# ### EDA 3

# In[7]:


df4 = pd.read_csv("day_wise.csv")


# In[8]:


df4.head()


# In[9]:


df4["Date"] = pd.to_datetime(df4["Date"])
df4["Date"]


# In[10]:


df4["Date"] = pd.to_datetime(df4["Date"])
df4["Day"] = pd.DatetimeIndex(df4["Date"]).day
df4["month"] = pd.DatetimeIndex(df4["Date"]).month
df4["year"] = pd.DatetimeIndex(df4["Date"]).year


# In[11]:


df4


# In[12]:


df4 = df4.drop(["Date"] , axis=1)
df4


# In[13]:


df4


# In[ ]:




