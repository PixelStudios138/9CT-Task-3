import pandas as pd
import matplotlib.pyplot as plt
import data_module as dm

df = pd.read_csv("Album Streams.csv")

# Convert the string columns to integers by removing commas
df['Total Streams'] = df['Total Streams'].str.replace(',', '').astype(int)
df['Artist Streams'] = df['Artist Streams'].str.replace(',', '').astype(int)

# Sort the csv file for the albums with the top 10 most streams and save it to a new dataset
sorted_by_artist = df.sort_values(by='Total Streams', ascending=False).head(10)

# Count albums for each artist
artist_counts = df['Artist'].value_counts()

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
        dm.plot_top_albums(sorted_by_artist, df)
    elif choice == '2':
        # Display the artist/album share
        dm.plot_album_artists(artist_counts)
    elif choice == '3':
        artist_name = input("Enter the name of the artist: ")
        if artist_name in df['Artist'].values:
            artist_data = df[df['Artist'] == artist_name]
            dm.plot_top_albums(artist_data, artist_data)
        else:
            print("Artist not found in the dataset.")
    elif choice == '4':
        # Display the dataset
        print(df)
    elif choice == 'q':
        # Exit the program
        quit()