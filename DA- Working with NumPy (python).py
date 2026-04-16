import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # --- Assessment 1: Banklist Analysis ---

#load the data
banks = pd.read_csv('F:/aasignment/1/numpy,panda,matplotlit/banklist.csv')

# 1) Import pandas and read in the banklist.csv file into a dataframe called banks.
print(banks)

# 2) Show the head of the dataframe.
print(banks.head())

# 3) What are the column names?
print(banks.columns)

# 4) How many States (ST) are represented in this data set?
print(len(banks['ST'].unique()))  

# 5) Get a list or array of all the states in the data set.
print(banks['ST'].unique())

# 6) What are the top 5 states with the most failed banks?
print(banks['ST'].value_counts().head(5))

# 7) What are the top 5 acquiring institutions?
print(banks['Acquiring Institution'].value_counts().head(5)) 

# 8) How many banks has the State Bank of Texas acquired? How many of
# them were actually in Texas?
print(banks[banks['Acquiring Institution'] == 'State Bank of Texas'].shape[0])
print(len(banks[(banks['Acquiring Institution'] == 'State Bank of Texas') & (banks['ST'] == 'TX')]))

# 9) What is the most common city in California for a bank to fail in?
print(banks[(banks['ST'] == 'CA')]['City'].value_counts().idxmax()) 



# --- Assessment 2: Historical Automobile Sales ---

#load the data
df = pd.read_csv('F:/aasignment/1/numpy,panda,matplotlit/historical_automobile_sales.csv')


# Q 1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year.
df.groupby('Year')['Automobile_Sales'].mean().plot(kind='line', title='Automobile Sales Over Years')
plt.show()


# Q 2: Plot different lines for categories of vehicle type and analyze the trend
# to answer the question Is there a noticeable difference in sales trends
# between different vehicle types during recession periods?
df.pivot_table(index='Year', columns='Vehicle_Type', values='Automobile_Sales').plot(kind='line')
plt.title('Sales Trend by Vehicle Type')
plt.show()



# Q 3: Use the functionality of Seaborn Library to create a visualization to compare
# the sales trend per vehicle type for a recession period with a non- recession
# period.
plt.figure(figsize=(10, 6))
sns.barplot(x='Vehicle_Type', y='Automobile_Sales', hue='Recession', data=df)
plt.title('Average Automobile Sales during Recession and Non-Recession')
plt.xticks(rotation=45)
plt.show()

# Q 4: Now you want to compare the sales of different vehicle types
# during a recession and a non-recession period









