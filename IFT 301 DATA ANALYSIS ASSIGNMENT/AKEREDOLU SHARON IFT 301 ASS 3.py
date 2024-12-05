# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:41:11 2024

@author: SHARON AKEREDOLU
"""

import matplotlib.pyplot as plt

# Data for plant growth with and without music
growth_with_music = [
    304, 257, 174, 214, 69, 317, 387, 47, 157, 0,
    332, 308, 317, 286, 236, 299, 206, 278, 188, 43,
    0, 0, 0, 0, 0
]

growth_without_music = [
    292, 270, 47, 288, 324, 292, 364, 316, 287, 75,
    282, 149, 274, 319, 213, 3, 324, 2, 128, 219,
    94, 164, 0, 0, 0
]

# Function to create dot plots
def create_dot_plot(data, title, ax):
    ax.scatter(data, [1] * len(data), alpha=0.7, color='blue')
    ax.set_title(title)
    ax.set_xlabel("Plant Growth (mm)")
    ax.set_yticks([])
    ax.grid(axis='x', linestyle='--', alpha=0.7)

# Function to create histograms
def create_histogram(data, title, ax, bins=10):
    ax.hist(data, bins=bins, alpha=0.7, color='orange', edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel("Plant Growth (mm)")
    ax.set_ylabel("Frequency")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# Create subplots for dot plots and histograms
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(hspace=0.4)

# Dot plots
create_dot_plot(growth_with_music, "Dot Plot: Growth with Music", axs[0, 0])
create_dot_plot(growth_without_music, "Dot Plot: Growth without Music", axs[0, 1])

# Histograms
create_histogram(growth_with_music, "Histogram: Growth with Music", axs[1, 0], bins=10)
create_histogram(growth_without_music, "Histogram: Growth without Music", axs[1, 1], bins=10)

# Display the plots
plt.show()