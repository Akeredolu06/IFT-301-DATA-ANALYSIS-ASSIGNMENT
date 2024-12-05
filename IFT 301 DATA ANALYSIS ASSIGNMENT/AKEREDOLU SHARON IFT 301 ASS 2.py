# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:39:20 2024

@author: SHARON AKEREDOLU
"""

# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data for females and males
female_breath_held = [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66]
male_breath_held = [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]

# Combine the data to ignore sex for the histogram
combined_breath_held = female_breath_held + male_breath_held

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(combined_breath_held, bins=8, edgecolor='black', alpha=0.7)
plt.title("Histogram of Breath-Holding Times (Ignoring Sex)")
plt.xlabel("Breath-Holding Time (seconds)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Create a DataFrame for the side-by-side dot plot
import pandas as pd

# Creating a DataFrame
data = {
    'Breath_Held': female_breath_held + male_breath_held,
    'Sex': ['Female']*len(female_breath_held) + ['Male']*len(male_breath_held)
}

df = pd.DataFrame(data)

# Side-by-side dot plot using Seaborn
plt.figure(figsize=(10, 6))
sns.stripplot(x='Sex', y='Breath_Held', data=df, jitter=True, palette='Set2', dodge=True)
plt.title("Side-by-Side Dot Plot of Breath-Holding Times by Sex")
plt.xlabel("Sex")
plt.ylabel("Breath-Holding Time (seconds)")
plt.grid(True)
plt.show()