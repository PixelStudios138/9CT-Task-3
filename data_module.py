# Function to show a plot of the top 10 albums and each artists stream
def plot_top_albums(artist_dataset):
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
    plt.savefig("most_popular_albums.png")
    plt.show()