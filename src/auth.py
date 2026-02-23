import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

SCOPE = "user-read-recently-played user-top-read user-read-currently-playing"

def get_spotify_client() -> spotipy.Spotify:
    """OAuth 인증된 Spotipy 클라이언트를 반환합니다."""
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=SCOPE,
        cache_path=".cache"
    ))