# Added imports to use for EDA
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# Put the CSV file into a DataFrame
data = pd.read_csv("data/nba_player_stats_2025.csv")
df = pd.DataFrame(data = data, columns = data.columns)

# Basic Summary statistics
print(df.head())
print(df.info())
print(df.isnull().sum())