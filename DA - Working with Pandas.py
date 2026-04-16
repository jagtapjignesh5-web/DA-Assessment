import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#----- Assessment 1: Financial Analysis  -----

#load the data
df = pd.read_csv("F:/aasignment/1/numpy,panda,matplotlit,seaborn/finance_economics_dataset.csv")

# 1. What is the shape of the dataset?
print(f"  Rows    : {df.shape[0]:,}")
print(f"  Columns : {df.shape[1]}")

# 2. What are the column names and their data types?
print(df.dtypes)

# 3. How many unique stock indices are there?
print( len(df['Stock Index'].unique()))

# 4. What is the date range of the dataset?
print(f"  Date Range: {df['Date'].min()} to {df['Date'].max()}")

# 5. Are there any missing values?
print(df.isnull().sum())

# 6. Are there negative values in columns that should be non-negative?
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    print(col, ":", (df[col] < 0).sum())

# 7. What is the summary of GDP Growth (%)?
print(df['GDP Growth (%)'].describe())

# 8. Are there rows with zero or near-zero trading volume? 
print((df['Trading Volume'] <= 1).sum())

# 9. Are there any duplicate rows?
print(df.duplicated().sum())

# 10. Are there outliers in GDP, Gold, or Oil prices?
for col in ['GDP Growth (%)', 'Gold Price (USD per Ounce)', 'Crude Oil Price (USD per Barrel)']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(col, ":", len(outliers))

# 11. What is the summary of Inflation Rate (%)?
print(df['Inflation Rate (%)'].describe())

# 12. What is the average unemployment rate?
print(df['Unemployment Rate (%)'].mean())

# 13. Which index has the highest trading volume?
print(df.groupby('Stock Index')['Trading Volume'].mean().idxmax())

# 14. How many stock records are from each index?
print(df['Stock Index'].value_counts())

# 15. What is the correlation between inflation and interest rate?
print(df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

# 16. What is the average Consumer Confidence Index?
print(df['Consumer Confidence Index'].mean())

# 17. Which column has the highest standard deviation?
std_devs = df.select_dtypes(include='number').std()
print(std_devs.idxmax(), ":", std_devs.max())

# 18. What is the highest gold price recorded?
print(df['Gold Price (USD per Ounce)'].max())

# 19. Which date had the highest crude oil price?
print(df.loc[df['Crude Oil Price (USD per Barrel)'].idxmax(), 'Date'])

# 20. What is the average corporate profit?
print(df['Corporate Profits (Billion USD)'].mean())


#----  Insightful Analysis Questions  ----

# 1. What percentage of the dataset shows negative GDP growth?
print((df['GDP Growth (%)'] < 0).sum() / len(df) * 100)

# 2. Does high inflation correspond to higher interest rates?
print(df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

# 3. Is there a relationship between unemployment and consumer spending?
print(df['Unemployment Rate (%)'].corr(df['Consumer Spending (Billion USD)']))

# 4. Do higher corporate profits align with higher consumer confidence?
print(df['Corporate Profits (Billion USD)'].corr(df['Consumer Confidence Index']))

# 5. What’s the trend of crude oil prices over time?
df['Date'] = pd.to_datetime(df['Date'])
sns.lineplot(x='Date', y='Crude Oil Price (USD per Barrel)', data=df)
plt.show()

# 6. Are gold prices inversely related to stock performance?
print(df['Gold Price (USD per Ounce)'].corr(df['Close Price']))

# 7. Does government debt impact consumer confidence?
print(df['Government Debt (Billion USD)'].corr(df['Consumer Confidence Index']))

# 8. How do mergers & acquisitions (M&A) activity correlate with stock index closing prices?
print(df['Mergers & Acquisitions Deals'].corr(df['Close Price']))

# 9. Is retail sales growth associated with GDP growth?
print(df['Retail Sales (Billion USD)'].corr(df['GDP Growth (%)']))

# 10. Is stock market performance linked to consumer spending?
print(df['Close Price'].corr(df['Consumer Spending (Billion USD)']))

# 11. Which stock index had the highest average closing price?
print(df.groupby('Stock Index')['Close Price'].mean().idxmax())

# 12. What is the relationship between interest rate and unemployment?
print(df['Interest Rate (%)'].corr(df['Unemployment Rate (%)']))

# 13. Do lower consumer confidence values coincide with higher bankruptcy rates?
print(df['Consumer Confidence Index'].corr(df['Bankruptcy Rate (%)']))

# 14. Which indicator has the highest correlation with stock close price?
numeric_cols = df.select_dtypes(include='number').columns
correlations = df[numeric_cols].corr()['Close Price'].drop('Close Price')
print(correlations.idxmax(), ":", correlations.max())

# 15. Are unemployment rates lower when corporate profits are high?
print(df['Unemployment Rate (%)'].corr(df['Corporate Profits (Billion USD)']))





#----- Assessment 2: Retail Data  -----

#load the data
df1 = pd.read_csv("F:/aasignment/1/numpy,panda,matplotlit,seaborn/Retail Data.csv")

# 1. View the structure of the dataset (columns, types, missing values).
print(df1.info())

# 2. What is the shape (rows, columns) of the dataset?
print(df1.shape)

# 3. Are there any duplicate records?
print(df1.duplicated().sum())

# 4. Are there any missing or corrupted entries in Ship Date, Order Date, or numeric columns?
print("Missing values:", df1.isnull().sum())

# 5. Convert Order Date and Ship Date to datetime.
df1['Order Date'] = pd.to_datetime(df1['Order Date'], errors='coerce')
df1['Ship Date'] = pd.to_datetime(df1['Ship Date'], errors='coerce')


# 6. Check for future or inconsistent shipping dates.
invalid_dates = df1[(df1['Ship Date'] < df1['Order Date']) | 
                   (df1['Ship Date'] > pd.Timestamp.today())]
print("Invalid dates:", len(invalid_dates))

# 7. Convert price columns to numeric (remove $ and commas).
for col in df1.columns:
    if df1[col].dtype == 'object':
        try:
            df1[col] = df1[col].replace('[\$,]', '', regex=True).astype(float)
        except:
            pass

# 8. What are the unique values in Customer Type and Order Priority?
print("Customer Type:", df1['Customer Type'].unique())    
print("Order Priority:", df1['Order Priority'].unique())

# 9. What are the most common shipping modes?
print(df1['Ship Mode'].value_counts())

# 10. Which cities have the highest number of orders?
print(df1['City'].value_counts().head(10))

# 11. What’s the range of order quantities and prices?
print("Quantity Range:", df1['Order Quantity'].min(), df1['Order Quantity'].max())
print("Sales Range:", df1['Sub Total'].min(), df1['Sub Total'].max())

# 12. Create a new column for shipping duration.
df1['Shipping Duration'] = (df1['Ship Date'] - df1['Order Date']).dt.days
print(df1)

# 13. Are there any orders with zero or negative total or quantity?
print("Zero/Negative Quantity:", (df1['Order Quantity'] <= 0).sum())

# 14. Are all discount percentages matching discount dollar amounts?
calc_discount = df1['Sub Total'] * df1['Discount %'] / 100
print("Discount mismatch:",
      (abs(calc_discount - df1['Discount']) > 1).sum())

# 15. Check for mismatches in total calculation'
df1['Sub Total'] = pd.to_numeric(df1['Sub Total'], errors='coerce')
df1['Discount %'] = pd.to_numeric(df1['Discount %'], errors='coerce')
calc_total = df1['Sub Total'] - df1['Discount %'] + df1['Shipping Cost']
print("Total mismatch:",
      (abs(calc_total - df1['Total']) > 1).sum())   

# 16. Identify top 5 products by order quantity.
top_products = df1.groupby('Product Name')['Order Quantity'].sum().sort_values(ascending=False).head(5)
print(top_products)

# 17. Which Account Manager handled the most revenue?
top_manager = df1.groupby('Account Manager')['Total'].sum().idxmax()
print("Top Account Manager:", top_manager)

# 18. What is the average shipping cost by mode?
avg_shipping_cost = df1.groupby('Ship Mode')['Shipping Cost'].mean()
print(avg_shipping_cost)

# 19. Find the most profitable product.
profit_by_product = df1.groupby('Product Name')['Total'].sum().idxmax()
print("Most Profitable Product:", profit_by_product)



#----  Insightful Analysis Questions  ----

# 1. What is the total revenue generated across all orders?
total_revenue = df1['Total'].sum()
print("Total Revenue:", total_revenue)

# 2. Which customer type generates more revenue?
revenue_by_customer = df1.groupby('Customer Type')['Total'].sum()
print("Revenue by Customer Type:\n", revenue_by_customer)

# 3. How does order priority affect revenue?
revenue_by_priority = df1.groupby('Order Priority')['Total'].sum()
print("Revenue by Order Priority:\n", revenue_by_priority)

# 4. What is the average profit margin by product category?
df1['Profit Margin'] = (df1['Total'] - df1['Sub Total']) / df1['Sub Total'] * 100
avg_profit_margin = df1.groupby('Product Category')['Profit Margin'].mean()
print("Average Profit Margin by Product Category:\n", avg_profit_margin)

# 5. What is the most profitable product overall?
profit_by_product = df1.groupby('Product Name')['Total'].sum().idxmax()
print("Most Profitable Product:", profit_by_product)

# 6. How many days does it usually take to ship an order?
df1['Shipping Duration'] = (df1['Ship Date'] - df1['Order Date']).dt.days
avg_shipping_duration = df1['Shipping Duration'].mean()
print("Average Shipping Duration (days):", avg_shipping_duration)

# 7. Do longer shipping times impact profit margins?
df1['Profit Margin'] = (df1['Total'] - df1['Sub Total']) / df1['Sub Total'] * 100
correlation = df1['Shipping Duration'].corr(df1['Profit Margin'])
print("Correlation between Shipping Duration and Profit Margin:", correlation)

# 8. Which city brings in the highest revenue?
revenue_by_city = df1.groupby('City')['Total'].sum().idxmax()
print("City with Highest Revenue:", revenue_by_city)

# 9. Which account manager generated the most revenue?
revenue_by_manager = df1.groupby('Account Manager')['Total'].sum().idxmax()
print("Account Manager with Highest Revenue:", revenue_by_manager)

# 10. Which shipping mode is most cost-effective (lowest avg. shipping)?
avg_shipping_cost = df1.groupby('Ship Mode')['Shipping Cost'].mean().idxmin()
print("Most Cost-Effective Shipping Mode:", avg_shipping_cost)

# 11. Do higher discounts reduce profits?
df1['Profit Margin'] = (df1['Total'] - df1['Sub Total']) / df1['Sub Total'] * 100
correlation = df1['Discount %'].corr(df1['Profit Margin'])
print("Correlation between Discount % and Profit Margin:", correlation)

# 12. Which state has the highest number of orders?
orders_by_state = df1.groupby('State')['Order No'].count().idxmax()
print("State with Highest Number of Orders:", orders_by_state)

# 13. What is the average discount % across all orders?
avg_discount = df1['Discount %'].mean()
print("Average Discount %:", avg_discount)

# 14. What is the average total spend per order?

avg_total_spend = df1['Total'].mean()
print("Average Total Spend per Order:", avg_total_spend)

# 15. . Are certain containers (e.g., Small Box, Wrap Bag) more profitable?
result = df.groupby('Product Container')['Profit Margin'].mean().sort_values(ascending=False)

print(result)