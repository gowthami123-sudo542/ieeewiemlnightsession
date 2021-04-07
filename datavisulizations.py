#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(color_codes=True)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


auto=pd.read_csv("E:\\csv files\\Automobile (1).csv")


# In[18]:


auto.tail(5)


# In[9]:


sns.distplot(auto["normalized_losses"]) #gives the  univarinant distribution of the continous values
plt.show()


# In[10]:


sns.distplot(auto["normalized_losses"],kde=False,rug=True) #within the bins frequency more line means more concentration
plt.show()


# In[11]:


sns.jointplot(auto["engine_size"],auto["horsepower"]) #To analyze two continous values features by joint plot
plt.show()


# In[12]:


sns.jointplot(auto["engine_size"],auto["horsepower"],kind="kde") #density are formed
plt.show()


# In[13]:


sns.jointplot(auto["engine_size"],auto["horsepower"],kind="resid") #creating error points in regression
plt.show()


# In[14]:


sns.jointplot(auto["engine_size"],auto["horsepower"],kind="hex")
plt.show()


# In[15]:


sns.jointplot(auto["engine_size"],auto["horsepower"],kind="reg")
plt.show()


# In[15]:


sns.pairplot(auto[["normalized_losses","engine_size","horsepower"]]) #mutiple variant analyze in a singal plot


# In[20]:



sns.stripplot(auto["fuel_type"],auto["horsepower"],jitter=True)#,showing the relation between catergorical value and continuos variable


# In[14]:


sns.swarmplot(auto["fuel_type"],auto["horsepower"])#values does not overlap each other frequecy of values at each level


# In[22]:


sns.boxplot(auto["number_of_doors"],auto["horsepower"],hue=auto["fuel_type"]) #if the interquartile region is greater then those feture are considered as outliers


# In[24]:


sns.barplot(auto["body_style"],auto["horsepower"],hue=auto["engine_location"])#that line indicates confidence level ,0 is also include


# In[25]:


sns.countplot(auto["body_style"],hue=auto["engine_location"]) #shows the frequency values ,here only one value is passed


# In[27]:


sns.pointplot(auto["fuel_system"],auto["horsepower"],hue=auto["number_of_doors"])#shows the high points and connects the points 


# In[28]:


sns.factorplot(x="fuel_type",y="horsepower",hue="number_of_doors",col="engine_location",data=auto,kind="swarm") #used for mulitple cateogical values


# In[29]:


sns.lmplot(x="horsepower",y="peak_rpm",data=auto,hue="fuel_type") #used for linear regression


# In[ ]:





# In[ ]:




