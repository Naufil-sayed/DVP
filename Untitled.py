#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("Workout.csv")


# In[2]:


print(data)


# In[4]:


excel=pd.read_excel("Workout.xlsx")


# In[5]:


print(excel)


# In[6]:


from IPython import display
display.Image("C:/Users/Student/Documents/dss/image1.jpeg")


# In[7]:


from IPython import display
display.Image("image1")


# In[8]:


import matplotlib.imagempimg
img=mpimg.imread("image1.jpeg")
plt.imshow(img)


# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# plt.imshow(mpimg.imread('image1.jpg'))

# In[ ]:




