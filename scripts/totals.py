import pandas as pd

data_total = pd.read_csv("data/BB_totals_2024_2025.csv")
dft = pd.DataFrame(data = data_total, columns = data_total.columns)

# Basic Summary statistics
print(dft.head())  
print(dft.info())
print(dft.isnull().sum())
print(dft.summary())