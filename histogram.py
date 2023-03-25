#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


# In[65]:


a=[2,34,5,6,9,5,4,2,33,55]
means=np.mean(np.array(a))
#ypoint=np.array(a)
plt.plot(a, marker = '1',color='green')
plt.show()


# In[61]:


a=[2,34,5,6,9,5,4,2,33,55]
ypoint=np.array(a)
plt.plot(ypoint, 'o-r')
plt.show()


# In[120]:


ages=[23,55,78,10,32,78,44,41,25,28,29,30]
#Calculating Mean
mean_ages=np.mean(np.array(ages))
#Calculating Median
median_age=np.median(np.array(ages))
#Calculating Variance
variance_age=np.var(np.array(ages))
#std_ages=np.std(np.arange(ages))
plt.hist(ages, edgecolor='Black')
plt.title('People Ages',loc='Right')
plt.axvline(mean_ages, color='Green', linewidth=1, label='Age Mean')
plt.axvline(median_age, color='Red', linewidth=1, label='Age Median')
plt.axvline(variance_age, color='Orange', linewidth=1, label='Age Variace')
plt.xlabel('Ages')
plt.ylabel('Total Respondants')
plt.tight_layout()
plt.autoscale=True 
#plt.plot(ages,marker='1')
plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.show()
print('Mean',np.mean(ages,dtype=np.int32),'Median',np.median(ages),'Variance',np.var(ages))


# In[111]:


student=[1,2,3,4,5,6,875,4,22,445,72,63,64,28,90,74,23,87,29,27,877,33]
mean_students=np.mean(np.array(student))
plt.hist(student,edgecolor='Black')
plt.title('TotalGrades')
ax=plt.axvline(mean_students, color='Red', linewidth=1, label='Student Grades Median')
plt.xlabel('Grades')
plt.ylabel('Total No')
plt.autoscale=True
plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
plt.show()


# In[90]:



x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
#lable=['Apple','Banana','Orange','Grape','Lemon','Gava','Peanut','Strawberry','PineApple','Spanish','BLack Orange']
#plt.plot(lable)
plt.plot(x,y)
plt.legend()
#for printing back ground lines 
plt.grid(color='Green',linestyle=':',linewidth='1')
plt.show()


# In[107]:



y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(loc='upper left',borderpad=0)
plt.show() 


# In[110]:



y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
#OUTSIDE THE BOX 
plt.legend(bbox_to_anchor=(1.02,1),loc='upper left',borderaxespad=0)
plt.show() 


# In[ ]:




