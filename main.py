import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Album Streams.csv")

#print(df['Artist'].value_counts())

#chisel_data = df[df['Artist'] == 'Cold Chisel']
#print(chisel_data)

# Convert the string columns to integers by removing commas
df['Total Streams'] = df['Total Streams'].str.replace(',', '').astype(int) #replace the string using astype which is a special method
#df['Artist Streams'] = df['Artist Streams'].str.replace(',', '').astype(int) 

sorted_by_artist = df.sort_values(by='Total Streams', ascending=False)
print(sorted_by_artist[['Album', 'Artist', 'Total Streams']].head())

sorted_by_artist = sorted_by_artist['Albums'].value_counts().head()

# Create a bar chart with albums on x-axis and streams on y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot Total Streams
ax1.bar(sorted_by_artist['Album'], sorted_by_artist['Total Streams'], color='skyblue', alpha=0.7)
ax1.set_title('Total Streams by Album')
ax1.set_xlabel('Album')
ax1.set_ylabel('Total Streams')
ax1.tick_params(axis='x', rotation=45)
# Format y-axis to show values in millions
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

# Plot Artist Streams
ax2.bar(sorted_by_artist['Album'], sorted_by_artist['Artist Streams'], color='lightcoral', alpha=0.7)
ax2.set_title('Artist Total Streams')
ax2.set_xlabel('Album')
ax2.set_ylabel('Artist Streams')
ax2.tick_params(axis='x', rotation=45)
# Format y-axis to show values in millions
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

plt.tight_layout()
plt.show()

# Alternative: Combined bar chart
fig, ax = plt.subplots(figsize=(12, 6))
x = range(len(df))
width = 0.35

ax.bar([i - width/2 for i in x], df['Total Streams'], width,
       label='Total Streams', color='skyblue', alpha=0.7)
ax.bar([i + width/2 for i in x], df['Artist Streams'], width,
       label='Artist Streams', color='lightcoral', alpha=0.7)

ax.set_xlabel('Albums')
ax.set_ylabel('Streams')
ax.set_title('Album vs Artist Streams Comparison')
ax.set_xticks(x)
ax.set_xticklabels(sorted_by_artist['Album'], rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
ax.legend()

plt.tight_layout()
plt.show()

"""
sorted_by_artist.plot(kind='bar', title='Top 25 Albums by Total Streams')
plt.xlabel('Album')
plt.ylabel('Total Streams')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_25_albums.png")
plt.show()

# Count albums for each artist
artist_counts = df['Artist'].value_counts()
#print(artist_counts)

artist_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Albums by Artist')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("artist_pie_chart.png")
#plt.show()
"""