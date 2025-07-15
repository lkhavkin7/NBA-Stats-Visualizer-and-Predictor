import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


data_total = pd.read_csv("data/BB_totals_2024_2025.csv")
df = pd.DataFrame(data = data_total, columns = data_total.columns)


clean_df = df.dropna(subset=['Player', 'PTS'])
df_unique = clean_df.drop_duplicates(subset=['Player'], keep='first')
dft = df_unique.drop(["Awards", "Player-additional" ], axis = 1)
print(dft.isnull().sum())

top_10 = dft.sort_values(by='PTS', ascending=False).head(10).sort_values(by='PTS')


sns.set_theme(style="whitegrid", font_scale=1.15)
plt.figure(figsize=(11, 7))

# Create horizontal bar plot with a modern palette
bar = sns.barplot(
    data=top_10, 
    y='Player', 
    x='PTS', 
    palette='rocket',  # You can try 'plasma', 'viridis', etc.
    edgecolor='black'
)

# Add points values to each bar for clarity
for i, (value, name) in enumerate(zip(top_10['PTS'], top_10['Player'])):
    plt.text(value + 0.4, i, f'{value:.1f}', va='center', color='black', fontweight='bold')

plt.title('Top 10 Players by Points Scored in 2025 Season', fontsize=17, fontweight='bold')
plt.xlabel('Points Scored', fontsize=13)
plt.ylabel('Player', fontsize=13)
plt.gca().invert_yaxis()  # Invert y-axis to have the player with
plt.xticks(rotation=45)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()