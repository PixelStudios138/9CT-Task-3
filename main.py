import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Album Streams.csv")

# Convert the string columns to integers by removing commas
df['Total Streams'] = df['Total Streams'].str.replace(',', '').astype(int)
df['Artist Streams'] = df['Artist Streams'].str.replace(',', '').astype(int)

# Sort the csv file for the albums with the top 10 most streams and save it to a new dataset
sorted_by_artist = df.sort_values(by='Total Streams', ascending=False).head(10)

# Function to show a plot of the top 10 albums and each artists stream
def plot_top_albums():
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


    # Count albums for each artist
artist_counts = df['Artist'].value_counts()

# Function to show the share of albums per artist
def plot_album_artists():
    # Create a pie chart
    artist_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Albums by Artist')
    plt.ylabel('')  # Removes default y-axis label
    plt.tight_layout()
    # Save the chart as a png
    plt.savefig("artist_pie_chart.png")
    # Show the user the image
    plt.show()

print("Hello. How would you like to view data on these Australian artists? (Type the number of your choice)")
while True:
    # Provide some options for the user on how to view data
    print("1. Top 10 Albums by Total Streams & Artist Streams")
    print("2. Artist Distribution Pie Chart")
    print("3. Individual Artist Details")
    print("4. View the dataset")
    print("Q. Quit the program")

    choice = input("Enter your choice (1/2/3/4/q): ")
    if choice == '1':
        # Display the top albums
        plot_top_albums()
    elif choice == '2':
        # Display the artist/album share
        plot_album_artists()
    elif choice == '3':
        artist_name = input("Enter the name of the artist: ")
        if artist_name in df['Artist'].values:
            artist_data = df[df['Artist'] == artist_name]
            # Exact same code as the plot_top_albums() function, only with all the data for whatever artist the user chooses
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

            # Plot Total Streams
            ax1.bar(artist_data['Album'], artist_data['Total Streams'], color='skyblue', alpha=0.7)
            ax1.set_title('Total Streams by Album')
            ax1.set_xlabel('Album')
            ax1.set_ylabel('Total Streams')
            ax1.tick_params(axis='x', rotation=45)
            # Format y-axis to show values in millions
            ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

            # Plot Artist Streams
            ax2.bar(artist_data['Artist'], artist_data['Artist Streams'], color='lightcoral', alpha=0.7)
            ax2.set_title('Artist Total Streams')
            ax2.set_xlabel('Artist')
            ax2.set_ylabel('Artist Streams')
            ax2.tick_params(axis='x', rotation=45)
            # Format y-axis to show values in millions
            ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))

            plt.tight_layout()
            plt.savefig(f"{artist_name}_details.png")
            plt.show()            
        else:
            print("Artist not found in the dataset.")
    elif choice == '4':
        # Display the dataset
        print(df)
    elif choice == 'q':
        # Exit the program
        quit()