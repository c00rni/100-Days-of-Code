"""Class to interact with spotify API

This module wish allow to manage and interact with spotify API. The module use spotipy
(https://spotipy.readthedocs.io/en/2.22.1/)
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import urllib.parse

class Spotify:

    def __init__(self, username, client_id, client_secret) -> None:
        self._username = username
        self._client_id = client_id
        self._client_secret = client_secret

        scope = "user-read-private user-read-email playlist-modify-private"
        self.token = util.prompt_for_user_token(username=self._username,
                                           scope=scope,
                                           client_id=self._client_id,
                                           client_secret=self._client_secret)
        try:
            self.sp = spotipy.Spotify(auth=self.token)
        except Exception as e:
            raise ValueError(f"Can't get token for {self._username}")
    
    def getUserProfile(self) -> dict:
        results = self.sp.current_user()
        return results

    def getPreview(self, query:str):
        """Get the preview audio of a song

            https://developer.spotify.com/documentation/web-api/reference/search
        """
        urllib.parse.quote(query)
        return self.sp.search(query, limit=1, offset=0, type='track', market=None)

