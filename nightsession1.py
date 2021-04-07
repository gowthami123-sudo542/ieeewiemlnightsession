#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[6]:


age_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

plt.plot(age_x,py_dev_y,color="b",label="py_dev_y ")


js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
plt.plot(age_x,js_dev_y,color="g",linestyle=":",linewidth=3,label="js_dev_y")

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
plt.plot(age_x,dev_y,color="k",linestyle="--",linewidth=3,label="dev_y ")
plt.xlabel("ages")
plt.ylabel("Medain  Salary")
plt.title("Medain salary by ages")
plt.legend()#plt.legend(["All_dev","pyn_dev"])
plt.grid()
#plt.style.use("ggplot")
#plt.xkcd()
plt.show()
#plt.save_file("pathname")
plt.tight_layout()#used for padding
#print(plt.style.available)
#marker="."


# BARPLOT

# In[7]:


age1_x= [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_ind=np.arange(len(age1_x))
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
width=0.25
plt.bar(x_ind-width,py_dev_y,width=width,color="b",label="pyn_dev")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_ind,js_dev_y,width=width,color="g",label="js_dev")


dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_ind+width,dev_y,width=width,color="k",label="all_dev")
plt.xlabel("ages")
plt.ylabel("Medain  Salary")
plt.title("Medain salary by ages")
plt.legend()
plt.xticks(ticks=x_ind)
#plt.grid()
plt.style.use("ggplot")
plt.show()
#barh

PIECHART
# In[5]:


plt.style.use("fivethirtyeight")
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

plt.pie(slices,labels=labels,wedgeprops={"edgecolor":"black"})
plt.title("pie chart")
plt.tight_layout()
plt.show()


# In[8]:


plt.style.use("fivethirtyeight")
#slices=[120,80,30,20]
#labels=["120","80","30","20"]
#color=["black","blue","green","red"]
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java'] 
explode=[0.5,0,0,0,0]
plt.pie(slices,labels=labels,explode=explode,shadow=True,startangle=90,autopct="%2.2f%%",wedgeprops={"edgecolor":"black"})
plt.title("pie chart")
plt.tight_layout()
plt.show()


# STACKPLOT

# In[8]:


plt.style.use("fivethirtyeight")
mint = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
p2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
p3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
plt.stackplot(mint,p1,p2,p3,labels=["p1","p2","p3"])
plt.legend(loc="upper left")
plt.title("stack plot")
plt.tight_layout()
plt.show()


#HISTOGRAM(can create bins so we can see how many values can fall into the bin)
# In[9]:


ages=[18,19,21,25,26,26,30,32,38,45,55]


# In[10]:


plt.title("Age be Respondent")
plt.xlabel("Ages")
plt.ylabel("Total Respondent")
plt.hist(ages,bins=5,edgecolor="black")
#plt.legend()
plt.show()


# In[11]:


plt.style.use("seaborn")

x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
plt.scatter(x,y,s=sizes,c=colors,cmap="Greens",edgecolor="black",linewidth=1,alpha=0.75)#s is used to increase the size of the dot
cbar=plt.colorbar()
cbar.set_label("Satisfacation")


# In[9]:


from datetime import datetime,timedelta
from matplotlib import dates as mpl_dates
plt.style.use("seaborn")
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]
plt.plot_date(dates,y,linestyle="solid")
date_format=mpl_dates.DateFormatter('%Y,%d,%b')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.show()


# In[15]:


import pandas as pd
data=pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv")


# In[16]:


data.head()


# In[17]:


ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JavaScript')

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()


# In[20]:


fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
plt.tight_layout()

plt.show()


# In[19]:


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()


# In[ ]:




