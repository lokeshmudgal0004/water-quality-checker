#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
from MF_and_Visualization import pH, do, bod, nitrate, temp 


# In[2]:


# Define the range for Water Quality Index (WQI)
wqi_range = np.arange(-100, 200, 1)


# In[3]:


# Define fuzzy membership functions for WQI
wqi = ctrl.Consequent(wqi_range, 'WQI')


# In[4]:


wqi['Poor'] = fuzz.trimf(wqi_range, [0, 20, 40])
wqi['Moderate'] = fuzz.trimf(wqi_range, [30, 50, 70])
wqi['Good'] = fuzz.trimf(wqi_range, [60, 80, 100])


# In[5]:


# Define fuzzy rules
rule1 = ctrl.Rule(pH['Neutral'] & do['High'] & bod['Low'] & nitrate['Low'] & temp['Moderate'], wqi['Good'])
rule2 = ctrl.Rule(pH['Neutral'] & do['Medium'] & bod['Moderate'] & nitrate['Moderate'] & temp['Moderate'], wqi['Moderate'])
rule3 = ctrl.Rule(pH['Acidic'] & do['Low'] & bod['High'] & nitrate['High'] & temp['Warm'], wqi['Poor'])
rule4 = ctrl.Rule(pH['Alkaline'] & do['High'] & bod['Low'] & nitrate['Low'] & temp['Cold'], wqi['Good'])
rule5 = ctrl.Rule(pH['Neutral'] & do['High'] & bod['Moderate'] & nitrate['Moderate'] & temp['Moderate'], wqi['Moderate'])
rule6 = ctrl.Rule(pH['Acidic'] & do['Low'] & bod['High'] & nitrate['High'] & temp['Moderate'], wqi['Poor'])
rule7 = ctrl.Rule(pH['Neutral'] & do['Medium'] & bod['High'] & nitrate['High'] & temp['Warm'], wqi['Poor'])
rule8 = ctrl.Rule(pH['Alkaline'] & do['Low'] & bod['Moderate'] & nitrate['High'] & temp['Moderate'], wqi['Poor'])
rule9 = ctrl.Rule(pH['Neutral'] & do['Low'] & bod['Low'] & nitrate['Low'] & temp['Cold'], wqi['Moderate'])
rule10 = ctrl.Rule(pH['Neutral'] & do['High'] & bod['High'] & nitrate['Moderate'] & temp['Warm'], wqi['Moderate'])


# In[6]:


# Create a fuzzy control system
wqi_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
wqi_simulation = ctrl.ControlSystemSimulation(wqi_ctrl)


# In[7]:


# Plot WQI membership function
def plot_wqi():
    plt.figure(figsize=(7, 3))
    for label in wqi.terms:
        plt.plot(wqi.universe, wqi[label].mf, label=label)
    plt.title('Water Quality Index (WQI) Membership')
    plt.xlabel('WQI Score')
    plt.ylabel('Membership')
    plt.legend()
    plt.grid()
    plt.show()

plot_wqi()


# In[8]:


get_ipython().system('jupyter nbconvert --to script WaterQualitySystem.ipynb')


# In[ ]:





# In[ ]:





# In[ ]:




