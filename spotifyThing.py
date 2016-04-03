import sys
import spotipy
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyOAuth
scope = 'user-library-read'


def authorize():


    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri)

    return sp_oauth.get_authorize_url()
