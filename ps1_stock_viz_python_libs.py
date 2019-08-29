#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 1: Visualizing stock market performance using Python libraries

# (Due: 9/4/2019)
# 
# In this exercise you will demonstrate how to:
# 1. Import and use Python libraries
# 2. Load static data files
# 3. Use object attributes to display information about your data
# 4. Use object methods to manipulate your data
# 5. Perform a correlation between two datasets
# 6. Graph data using the matplotlib library
# 7. Your assignement
# 
# You'll also gain experience using documentation, selecting data, working with variables, and uploading to GitHub.

# #### 1. Import python libraries

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# #### 2. Load CSV file 
# Refer to the pandas documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

# In[9]:


tesla = pd.read_csv("TSLA.CSV")


# Type the variable name and see the data.

# In[10]:


tesla


# Notice that the index starts with "0".

# #### 3. Show information about the dataset using pandas DataFrame attributes.
# Refer to the pandas documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

# In[26]:


tesla.shape


# In[27]:


tesla.T


# In[28]:


tesla.columns


# In[29]:


tesla.dtypes


# In[30]:


tesla.values


# In[33]:


tesla.size
#this is just rows * columns


# In[34]:


tesla.empty


# #### 4. Use pandas DataFrame methods to show information and manipulate the dataset.

# Show descriptive statistics:

# In[36]:


tesla.describe()


# Show first five rows:

# In[37]:


tesla.head()


# Show correlations among features:

# In[38]:


tesla.corr()


# #### 5. Perform a correlation between two different datasets. We'll analyze Tesla's closing stock price and Ford's closing stock price.

# Load Ford's stock data:

# In[11]:


ford = pd.read_csv("F.CSV")


# Check to see it is loaded:

# In[39]:


ford.empty


# Check to see if the dimensions of each dataset are equal:

# In[42]:


tesla.shape == ford.shape


# Now perform the correlation:

# In[43]:


ford.corrwith(tesla)


# #### 6. Now let's practice plotting the data.
# 
# We will be using the 'Close' column of the Tesla dataset to analyze trends in the price of the stock since 2010.
# 
# Within the plot, we will also compute moving averages to determine whether Tesla stock has experienced the "death cross", which is a technical indicator.
# 
# * The death cross is a technical chart pattern indicating the potential for a major selloff.
# * The death cross appears on a chart when a stock’s short-term moving average crosses below its long-term moving average.
# * The death cross indicator has proven to be a reliable predictor of some of the most severe bear markets of the past century: 1929, 1938, 1974, and 2008
# * The death cross can be contrasted with a golden cross indicating a bull price movement.

# First, let's isolate the closing price data:

# In[18]:


tsla_clse = tesla.loc[:,'Close']


# Check the data:

# In[20]:


tsla_clse.head()


# Plot just the closing data using the matplotlib library which was imported in the first part:

# In[24]:


fig, ax = plt.subplots(figsize=(16,9))

ax.plot(tsla_clse.index, tsla_clse, label='TSLA')
ax.plot(tsla_clse.index, tsla_clse.rolling(window=50).mean(), Label='50-day moving average')
ax.plot(tsla_clse.index, tsla_clse.rolling(window=200).mean(), Label='200-day moving average')


ax.set_xlabel('Date')
ax.set_ylabel('Closing price($)')
ax.legend()
ax.legend()


# #### 7. Your assignment:
# * Import one Apple's stock price data. Make sure to download the CSV file into the correct directory.
# * Plot the same chart as we did for Tesla using Apple's data. 
# * Upload your jupyer notebook to GitHub and email me the link to your GitHub page.

# In[50]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[51]:


wazz = pd.read_csv("AAPL.CSV")


# In[52]:


wazz_clse = wazz.loc[:,'Close']


# In[53]:


wazz_clse.head()


# In[55]:


fig, ax = plt.subplots(figsize=(16,9))

ax.plot(wazz_clse.index, wazz_clse, label='APPL')
ax.plot(wazz_clse.index, wazz_clse.rolling(window=50).mean(), Label='50-day moving average')
ax.plot(wazz_clse.index, wazz_clse.rolling(window=200).mean(), Label='200-day moving average')


ax.set_xlabel('Date')
ax.set_ylabel('Closing price($)')
ax.legend()
ax.legend()


# In[ ]:




