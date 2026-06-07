# Project 7: Data Analysis with Pandas


import pandas as pd
# Load the dataset
data = pd.read_csv('data.csv')
# Display the first few rows of the dataset
print(data.head())
# Basic statistics about the dataset
print(data.describe())
# Check for missing values
print(data.isnull().sum())
# Data visualization
import matplotlib.pyplot as plt
# Plot a histogram of a specific column
plt.hist(data['column_name'], bins=20)
plt.title('Histogram of Column Name')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.show()
# Plot a scatter plot between two columns
plt.scatter(data['column_x'], data['column_y'])
plt.title('Scatter Plot of Column X vs Column Y')
plt.xlabel('Column X')
plt.ylabel('Column Y')
plt.show()
# Grouping data by a specific column and calculating the mean
grouped_data = data.groupby('group_column')['value_column'].mean()
print(grouped_data)
# Save the cleaned dataset to a new CSV file
data.to_csv('cleaned_data.csv', index=False)

