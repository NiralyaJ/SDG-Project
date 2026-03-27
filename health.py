import pandas as pd
import matplotlib.pyplot as plt

# Sample Health Dataset (Life Expectancy)
data = {
    "Year": [2000, 2005, 2010, 2015, 2020, 2022],
    "Life_Expectancy": [66, 68, 70, 72, 73, 74]  # years
}

df = pd.DataFrame(data)

print("Health Data Analysis (SDG 3)")
print("-----------------------------")
print("\nDataset:")
print(df)

# Basic Statistics
print("\nStatistics:")
print("Average Life Expectancy:", df["Life_Expectancy"].mean())
print("Maximum Year:", df.loc[df["Life_Expectancy"].idxmax(), "Year"])
print("Minimum Year:", df.loc[df["Life_Expectancy"].idxmin(), "Year"])

# Growth Calculation
df["Growth"] = df["Life_Expectancy"].pct_change() * 100
print("\nYearly Growth Rate (%):")
print(df[["Year", "Growth"]])

# Plot Graph
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Life_Expectancy"], marker='o')
plt.title("Life Expectancy Over Years")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.grid(True)
plt.show()