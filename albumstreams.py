import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials
client_id = "169d8d02f8f84e06b3ce71456104f176"
client_secret = "d61c2b785ea1431f9bd795b569401ec5"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_album_streams(album_name):
    """
    Retrieves the total streams for each song in a given album.

    Args:
        album_name (str): The name of the album.
    """
    # Search for the album
    results = sp.search(q='album:' + album_name, type='album')
    items = results['albums']['items']
    if not items:
        print(f"No album found with the name '{album_name}'.")
        return

    album_id = items[0]['id']

    # Get the tracks from the album
    tracks = sp.album_tracks(album_id)['items']

    total_streams = 0
    for track in tracks:
        track_id = track['id']
        track_name = track['name']

        # Get track audio features to access popularity (stream count)
        track_info = sp.track(track_id)
        streams = track_info['popularity']  # Popularity roughly corresponds to stream count

        print(f"Track: {track_name}, Streams: {streams}")
        total_streams += streams

    print(f"\nTotal streams for all tracks in the album: {total_streams}")

if __name__ == '__main__':
    album_name = input("Enter the name of the album: ")
    get_album_streams(album_name)