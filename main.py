import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

#URI for artists used in project
# A URI basically points to the artist on Spotify
screaming_jets_uri = 'spotify:artist:3vgQA38yGGMvn4DHjsVre5'
acdc_uri = 'spotify:artist:711MCceyCBcFnzjGY4Q7Un'
noiseworks_uri = 'spotify:artist:3IJFGnsUboabVEbJz1UR91'
cold_chisel_uri = 'spotify:artist:1VcbchGlIfo3Gylxc3F076'
jimmy_barnes_uri = 'spotify:artist:1k5aZWIOUbUfKcnMxtEivJ'
ian_moss_uri = 'spotify:artist:4RMdsc21y0aET1OCm32h1u'
icehouse_uri = 'spotify:artist:3IUisqn0mluZR0LITs8Sqk'
angels_uri = 'spotify:artist:2PeqTZKroEc2oDwTfmB2al'
midnight_oil_uri = 'spotify:artist:72KyoXzp0NOQij6OcmZUxk'
rose_tattoo_uri = 'spotify:artist:1WsfEkSfrPIhy1lK7ZLRRH'
inxs_uri = 'spotify:artist:1eClJfHLoDI4rZe5HxzBFv'
australian_crawl_uri = 'spotify:artist:41fDGRDlzczk5Yo2wDo0H4'
choirboys_uri = 'spotify:artist:2u6qHMpQaE48aowjWKJeCM'

client_id = "169d8d02f8f84e06b3ce71456104f176"
client_secret = "d61c2b785ea1431f9bd795b569401ec5"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Defining some variables. The artist_albums dictionary will hold the names of the albums for each artist
artist_albums = {}

# Function to retrieve and store albums for a given artist URI
def show_album(uri, name):
    albums_list = []
    # Search for the artist's albums using the provided URI
    results = sp.artist_albums(uri, album_type='album')
    # Create a list of albums for the artist
    albums = results['items']
    while results['next']:
        # Add each album to the list and continue until there are no more results
        results = sp.next(results)
        albums.extend(results['items'])
    # Store the album names in a list to use for the dictionary
    for album in albums:
        albums_list.append(album['name'])
    # Add the information to the dictionary. The key is the artist name and the value is the list of albums previously created
    artist_albums[name] = albums_list

# Retrieve and store albums for each artist
# There probably is a way to automate this, but that would take 5 more hours than I have
show_album(screaming_jets_uri, "The Screaming Jets")
show_album(acdc_uri, "AC/DC")
show_album(noiseworks_uri, "Noiseworks")
show_album(cold_chisel_uri, "Cold Chisel")
show_album(jimmy_barnes_uri, "Jimmy Barnes")
show_album(ian_moss_uri, "Ian Moss")
show_album(icehouse_uri, "Icehouse")
show_album(angels_uri, "The Angels")
show_album(midnight_oil_uri, "Midnight Oil")
show_album(rose_tattoo_uri, "Rose Tattoo")
show_album(inxs_uri, "INXS")
show_album(australian_crawl_uri, "Australian Crawl")
show_album(choirboys_uri, "The Choirboys")

# Convert the artist_albums dictionary to a DataFrame and save it to a CSV file
df = pd.DataFrame.from_dict(artist_albums, orient='index').transpose()
df.to_csv("artist_albums.csv", index=False)