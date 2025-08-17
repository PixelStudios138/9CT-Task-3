import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = "169d8d02f8f84e06b3ce71456104f176"
client_secret = "d61c2b785ea1431f9bd795b569401ec5"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='artist:The Screaming Jets track:Better', type='track')

print(results)

#df = pd.DataFrame(results)

#df.to_csv("Better.csv", index=False)