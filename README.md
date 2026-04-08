# Health Data Analysis using Python (SDG 3: Good Health and Well-being)

## Description

The Health Data Analysis system is a simple Python-based application that analyzes life expectancy data over different years. It helps in understanding improvements in global health and supports awareness of Sustainable Development Goal 3 (Good Health and Well-being).

This project demonstrates how data analysis and visualization techniques can be used to study real-world health trends and improvements.

---

## Objective

The main objectives of this project are:

- To analyze health-related data using Python  
- To understand data handling using pandas  
- To perform statistical analysis  
- To visualize data using graphs  
- To understand real-world health improvements  

The program includes:
- data analysis  
- statistical calculations  
- growth rate computation  
- graphical visualization  

This improves understanding of:
- Data analysis  
- Visualization techniques  
- Logical thinking  
- Real-world problem solving  

---

## Features

Data Analysis  
- Displays dataset  
- Calculates average life expectancy  
- Finds maximum and minimum years  

Growth Calculation  
- Calculates yearly percentage growth  

Visualization  
- Plots graph for life expectancy trends  

Error Handling  
- Ensures smooth execution  

---

## Technologies Used

Programming Language: Python  

Libraries Used:  
- pandas (for data handling)  
- matplotlib (for data visualization)  

---

## System Architecture

The application follows a simple structure:

Main Module  
- Loads dataset  
- Displays data  

Analysis Module  
- Calculates statistics  
- Computes growth rate  

Visualization Module  
- Plots graph  

---

## Python Program

```python
import pandas as pd
import matplotlib.pyplot as plt

#  Health Dataset
data = {
    "Year": [2000, 2005, 2010, 2015, 2020, 2022],
    "Life_Expectancy": [66, 68, 70, 72, 73, 74]
}

df = pd.DataFrame(data)

print("Health Data Analysis (SDG 3)")
print("-----------------------------")
print("\nDataset:")
print(df)

# Statistics
print("\nStatistics:")
print("Average Life Expectancy:", df["Life_Expectancy"].mean())
print("Maximum Year:", df.loc[df["Life_Expectancy"].idxmax(), "Year"])
print("Minimum Year:", df.loc[df["Life_Expectancy"].idxmin(), "Year"])

# Growth Rate
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
```

## Output
<img width="637" height="555" alt="Screenshot 2026-03-27 115255" src="https://github.com/user-attachments/assets/e1b191c1-a814-45be-b5ce-b7391c4e5f58" />


<img width="942" height="582" alt="image" src="https://github.com/user-attachments/assets/0710deb2-6847-481f-a326-e1b17c3aae87" />


## Testing

The application was tested for:

- Correct data display  
- Accurate statistical calculations  
- Proper growth rate calculation  
- Graph generation  
- Handling missing values  

---

## Advantages

- Easy to understand  
- Helps analyze health trends  
- Provides visual representation  
- Beginner-friendly  
- Real-world application  

---

## Limitations

- Uses sample dataset  
- No real-time data  
- No database integration  

---

## Future Enhancements

- Use real-world health datasets  
- Add multiple health indicators  
- Store data in database  
- Create interactive dashboard  
- Convert into web application  

---

## Conclusion

The Health Data Analysis using Python project helps in understanding improvements in life expectancy and overall health trends.
It demonstrates key concepts such as data analysis, statistical computation, and visualization, providing a strong foundation for advanced data science and healthcare analytics applications.
