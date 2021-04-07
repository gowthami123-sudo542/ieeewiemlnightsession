#!/usr/bin/env python
# coding: utf-8

# 

# In[2]:


import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


k1=pd.read_csv("E:\\csv files\\diabetes.csv")
k1.shape


# In[4]:


k1.head()


# In[7]:


#checking for the null values
k1.isnull().sum()
#k1.shape


# In[8]:


#data types
k1.info()


# In[9]:


#
k1.describe()


# In[7]:


#as the values cannot be zero for the gulcouse ,bloodpressure,insulin for normal humanbeigns we change the values by mean of that row
non_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for coloumn in non_zero:
    k1[coloumn] = k1[coloumn].replace(0,np.NaN)
    mean = int(k1[coloumn].mean(skipna = True))
    k1[coloumn] = k1[coloumn].replace(np.NaN, mean)
    print(k1[coloumn])


# In[11]:


non_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for coloumn in non_zero:
    mean = int(k1[coloumn].mean(skipna = True))
    k1[coloumn] = k1[coloumn].replace(0,mean)
    print(k1[coloumn])


# In[12]:


p=sns.pairplot(k1, hue = 'Outcome')


# In[13]:


x=k1.drop(columns="Outcome",axis="coulmn")


# In[14]:


x


# In[15]:


y=k1["Outcome"]


# In[16]:


y


# In[21]:


from sklearn.model_selection import train_test_split


# In[25]:


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)


# In[27]:


from sklearn.preprocessing import StandardScaler #this is used for standradzation of the model


# In[28]:


sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)


# In[29]:


import math
math.sqrt(len(y_test))


# In[31]:


from sklearn.neighbors import KNeighborsClassifier #now i am buliding up the model


# In[34]:


classifier = KNeighborsClassifier(n_neighbors=11,p=2,metric='euclidean')
classifier.fit(x_train,y_train)


# In[35]:


y_pred =  classifier.predict(x_test)
y_pred


# In[39]:


from sklearn.metrics import confusion_matrix


# In[40]:


cm= confusion_matrix(y_test,y_pred)
cm


# In[41]:


sns.heatmap(cm,annot=True)


# In[42]:


from sklearn.metrics import accuracy_score


# In[ ]:





# In[43]:


print(accuracy_score(y_test,y_pred))


# In[44]:


plt.figure(figsize=(5, 7))
ax = sns.distplot(k1['Outcome'], hist=False, color="r", label="Actual Value")
sns.distplot(y_pred, hist=False, color="b", label="Predicted Values", ax=ax)
plt.title('Actual vs Precited value for outcome')
plt.show()
plt.close()


# In[ ]:




