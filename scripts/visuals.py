import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/nba_player_stats_2025.csv")
df = pd.DataFrame(data = data, columns = data.columns)

clean_df = df.dropna(subset=['Player', 'PTS'])
df_unique = clean_df.drop_duplicates(subset=['Player'], keep='first')


top_10 = df_unique.sort_values(by='PTS', ascending=False).head(10)
print("Number of players in top_10:", top_10.shape[0])

sns.heatmap(df_unique.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()
plt.close()

# Visualizing the distribution of points scored by players
plt.figure(figsize=(10, 6))
top_10 = df_unique.sort_values(by='PTS', ascending=False).head(10)
plt.barh(top_10['Player'], top_10['PTS'], color='purple')
plt.xlabel('Points Scored')
plt.ylabel('Player')
plt.title('Top 10 Players by Points Scored in 2025 Season')
plt.gca().invert_yaxis()  # Invert y-axis to have the player with



plt.title('Top 10 Players by Points Scored in 2025 Season')
plt.show()