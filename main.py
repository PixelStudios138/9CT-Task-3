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

def show_album(uri, name):
    albums_list = []
    results = sp.artist_albums(uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        albums_list.append(album['name'])
    artist_albums[name] = albums_list

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

df = pd.DataFrame.from_dict(artist_albums, orient='index').transpose()
df.to_csv("artist_albums.csv", index=False)