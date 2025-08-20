import matplotlib.pyplot as plt

# Function to show the share of albums per artist
def plot_album_artists(artist_counts):
    # Create a pie chart
    artist_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Albums by Artist')
    plt.ylabel('')  # Removes default y-axis label
    plt.tight_layout()
    # Save the chart as a png
    plt.savefig("artist_pie_chart.png")
    # Show the user the image
    plt.show()

# Function to show a plot of the top 10 albums and each artists stream
def plot_top_albums(artist_dataset, df, artist_name):
    # Create a bar chart with albums on x-axis and streams on y-axis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot Total Streams
    ax1.bar(artist_dataset['Album'], artist_dataset['Total Streams'], color='skyblue', alpha=0.7)
    ax1.set_title('Total Streams by Album')
    ax1.set_xlabel('Album')
    ax1.set_ylabel('Total Streams')
    ax1.tick_params(axis='x', rotation=45)
    # Format y-axis to show values in millions
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

    # Plot Artist Streams
    ax2.bar(df['Artist'], df['Artist Streams'], color='lightcoral', alpha=0.7)
    ax2.set_title('Artist Total Streams')
    ax2.set_xlabel('Artist')
    ax2.set_ylabel('Artist Streams')
    ax2.tick_params(axis='x', rotation=45)
    # Format y-axis to show values in millions
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

    plt.tight_layout()
    plt.savefig(f"{artist_name}_albums.png")
    plt.show()
