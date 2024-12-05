# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:37:16 2024

@author: SHARON AKEREDOLU
"""

# Import necessary libraries
import matplotlib.pyplot as plt

# Define the data
ingredients = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.275, 0.175, 0.075, 0.275, 0.175]

# Create a bar chart
plt.figure(figsize=(8, 6))  # Set the figure size
plt.barh(ingredients, proportions, color='purple')  # Horizontal bar chart

# Add title and labels
plt.title('Proportion of Ingredients', fontsize=14)
plt.xlabel('Proportion', fontsize=12)
plt.ylabel('Ingredients', fontsize=12)

# Show the plot
plt.show()