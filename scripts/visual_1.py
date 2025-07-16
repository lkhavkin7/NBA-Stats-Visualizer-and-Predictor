import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data_total = pd.read_csv("data/BB_totals_2024_2025.csv")
dft = pd.DataFrame(data = data_total, columns = data_total.columns)

# Correlation matrix heatmap
corr = dft.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation')
plt.xticks(ticks=np.arange(len(corr.columns)), labels=corr.columns, rotation=45, ha='right', fontsize=10)
plt.yticks(ticks=np.arange(len(corr.index)), labels=corr.index, fontsize=10)
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.tight_layout()
plt.show()


print(corr['PTS'].sort_values(ascending=False))
