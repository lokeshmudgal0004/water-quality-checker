#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt


# In[2]:


# Define the range for each parameter based on dataset
pH_range = np.arange(6.0, 9.9, 0.1)
do_range = np.arange(0.4, 13.6, 0.1)
bod_range = np.arange(0.1, 105, 0.1)
nitrate_range = np.arange(0.03, 11.9, 0.1)
temp_range = np.arange(2, 38, 0.1)


# In[3]:


# Define fuzzy membership functions
pH = ctrl.Antecedent(pH_range, 'pH')
do = ctrl.Antecedent(do_range, 'DO')
bod = ctrl.Antecedent(bod_range, 'BOD')
nitrate = ctrl.Antecedent(nitrate_range, 'Nitrate')
temp = ctrl.Antecedent(temp_range, 'Temperature')


# In[4]:


# pH membership functions (Triangular)
pH['Acidic'] = fuzz.trimf(pH_range, [6.0, 6.5, 6.8])
pH['Neutral'] = fuzz.trimf(pH_range, [6.5, 7.5, 8.0])
pH['Alkaline'] = fuzz.trimf(pH_range, [7.8, 9.0, 9.9])


# In[5]:


# DO membership functions (Triangular)
do['Low'] = fuzz.trimf(do_range, [0.4, 2, 4])
do['Medium'] = fuzz.trimf(do_range, [3, 5.5, 8])
do['High'] = fuzz.trimf(do_range, [7, 10, 13.6])


# In[6]:


# BOD membership functions (Trapezoidal)
bod['Low'] = fuzz.trapmf(bod_range, [0.1, 1, 2, 3])
bod['Moderate'] = fuzz.trapmf(bod_range, [2, 5, 7, 10])
bod['High'] = fuzz.trapmf(bod_range, [8, 20, 50, 105])


# In[7]:


nitrate['Low'] = fuzz.trapmf(nitrate_range, [0.03, 0.5, 1, 2])
nitrate['Moderate'] = fuzz.trapmf(nitrate_range, [1.5, 3, 4, 6])
nitrate['High'] = fuzz.trapmf(nitrate_range, [5, 7, 9, 11.9])


# In[8]:


# Temperature membership functions (Triangular)
temp['Cold'] = fuzz.trimf(temp_range, [2, 8, 15])
temp['Moderate'] = fuzz.trimf(temp_range, [10, 20, 30])
temp['Warm'] = fuzz.trimf(temp_range, [25, 32, 38])


# In[9]:


# Plot membership functions
def plot_membership(var, title):
    plt.figure(figsize=(7, 3))
    found_valid_mf = False
    for label in var.terms:
        mf = var[label].mf
        if mf is not None:
            plt.plot(var.universe, mf, label=label)
            found_valid_mf = True
    if found_valid_mf:
        plt.title(title)
        plt.xlabel('Value')
        plt.ylabel('Membership')
        plt.legend()
        plt.grid()
        plt.show()


# In[10]:


# Plot each membership function
plot_membership(pH, 'pH Membership' )
plot_membership(do, 'Dissolved Oxygen Membership' )
plot_membership(bod, 'BOD Membership')
plot_membership(nitrate, 'Nitrate Membership')
plot_membership(temp, 'Temperature Membership')


# In[11]:


get_ipython().system('jupyter nbconvert --to script MF_and_Visualization.ipynb')


# In[ ]:




