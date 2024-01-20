import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from pprint import pprint

class Spotify:

    def __init__(self, username, client_id, client_secret) -> None:
        self._username = username
        self._client_id = client_id
        self._client_secret = client_secret
    
    def getUserProfile(self) -> dict:
        scope = "user-read-private user-read-email"
        token = util.prompt_for_user_token(username=self._username,
                                           scope=scope,
                                           client_id=self._client_id,
                                           client_secret=self._client_secret)
        try:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user()
            return results
        except Exception as e:
            raise ValueError(f"Can't get token for {self._username}")

        
