import pandas as pd
import matplotlib.pyplot as plt

# Create synthetic dataset
data = {
    'Album': [
        'Cold Chisel', 'Thriller', 'Back in Black', 'The Dark Side of the Moon',
        'Abbey Road', 'Rumours', 'Hotel California', 'Led Zeppelin IV',
        'The Wall', 'Born to Run', 'Purple Rain', 'Appetite for Destruction',
        'Nevermind', 'OK Computer', 'The Joshua Tree', 'Blonde on Blonde',
        'Pet Sounds', "Sgt. Pepper's", "What's Going On", 'Kind of Blue',
        'Astral Weeks'
    ],
    'Artist': [
        'Cold Chisel', 'Michael Jackson', 'AC/DC', 'Pink Floyd',
        'The Beatles', 'Fleetwood Mac', 'Eagles', 'Led Zeppelin',
        'Pink Floyd', 'Bruce Springsteen', 'Prince', "Guns N' Roses",
        'Nirvana', 'Radiohead', 'U2', 'Bob Dylan',
        'The Beach Boys', 'The Beatles', 'Marvin Gaye', 'Miles Davis',
        'Van Morrison'
    ],
    'Total Streams': [
        '114,464,979', '1,234,567,890', '987,654,321', '876,543,210',
        '765,432,109', '654,321,098', '543,210,987', '432,109,876',
        '321,098,765', '210,987,654', '345,678,901', '456,789,012',
        '567,890,123', '678,901,234', '789,012,345', '890,123,456',
        '123,456,789', '234,567,890', '345,678,912', '456,789,123',
        '567,891,234'
    ],
    'Artist Streams': [
        '480,666,355', '2,500,000,000', '1,800,000,000', '1,600,000,000',
        '3,200,000,000', '1,200,000,000', '1,100,000,000', '1,900,000,000',
        '1,600,000,000', '950,000,000', '800,000,000', '750,000,000',
        '850,000,000', '720,000,000', '1,300,000,000', '680,000,000',
        '520,000,000', '3,200,000,000', '420,000,000', '380,000,000',
        '350,000,000'
    ]
}

df = pd.DataFrame(data)

# Alternative: Read from CSV file
# df = pd.read_csv('your_file.csv')

print("Original DataFrame:")
print(df)
print(f"Data types:\n{df.dtypes}\n")

# Convert the string columns to integers by removing commas
df['Total Streams'] = df['Total Streams'].str.replace(',', '').astype(int)
df['Artist Streams'] = df['Artist Streams'].str.replace(',', '').astype(int)

print("After conversion:")
print(df)
print(f"Data types:\n{df.dtypes}")

# Create a graph showing streams on the vertical axis
import matplotlib.pyplot as plt

# Create a bar chart with albums on x-axis and streams on y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot Total Streams
ax1.bar(df['Album'], df['Total Streams'], color='skyblue', alpha=0.7)
ax1.set_title('Total Streams by Album')
ax1.set_xlabel('Album')
ax1.set_ylabel('Total Streams')
ax1.tick_params(axis='x', rotation=45)
# Format y-axis to show values in millions
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

# Plot Artist Streams
ax2.bar(df['Album'], df['Artist Streams'], color='lightcoral', alpha=0.7)
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
ax.set_xticklabels(df['Album'], rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
ax.legend()

plt.tight_layout()
plt.show()