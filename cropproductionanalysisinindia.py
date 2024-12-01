
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\Users\HP\Downloads\Crop Production data.csv" 
df = pd.read_csv(file_path)
#Data exploration
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Statistical Summary ---")
print(df.describe())
print("\n--- Null Values ---")
print(df.isnull().sum())
#DataCLeaning
print("\n--- Cleaning Data ---")
df.dropna(inplace=True)
print(f"Rows after cleaning: {df.shape[0]}")
#Analyze top crops by production
crop_production = df.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print("\n--- Top Crops by Production ---")
print(crop_production.head(10))
#Visualize production distribution by states for a specific year
year = 2014
state_production = df[df['Crop_Year'] == year].groupby('State_Name')['Production'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=state_production.values, y=state_production.index)
plt.title(f"Production by States in {year}")
plt.xlabel("Total Production")
plt.ylabel("State")
plt.show()
# Visualize production trends for a specific crop over the years
crop = 'Rice'
crop_data = df[df['Crop'] == crop]
trends = crop_data.groupby('Crop_Year')['Production'].sum()
plt.figure(figsize=(10, 6))
sns.lineplot(x=trends.index, y=trends.values)
plt.title(f"Production Trends for {crop}")
plt.xlabel("Year")
plt.ylabel("Total Production")
plt.grid()
plt.show()
#Plot a correlation heatmap
numeric_data = df.select_dtypes(include=[np.number])
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
#Generate insights
print("\n--- Key Insights ---")
print("1. Top crops by production show variations based on years.")
print("2. States like Punjab and Uttar Pradesh consistently lead in production.")
print("3. Production trends for major crops indicate seasonal and market-driven impacts.")

