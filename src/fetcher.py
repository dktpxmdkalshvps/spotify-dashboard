import spotipy

def fetch_recently_played(sp: spotipy.Spotify, limit: int = 50) -> list[dict]:
    results = sp.current_user_recently_played(limit=limit)
    items = results.get("items", [])

    merged = []
    for item in items:
        track = item["track"]

        merged.append({
            "played_at":        item["played_at"],
            "track_name":       track["name"],
            "artist":           track["artists"][0]["name"],
            "artist_id":        track["artists"][0]["id"],
            "album":            track["album"]["name"],
            "album_type":       track["album"]["album_type"],   # single/album/compilation
            "track_id":         track["id"],
            "track_popularity": track.get("popularity", 0),
            "duration_ms":      track["duration_ms"],
            "explicit":         track.get("explicit", False),
            "total_tracks":     track["album"].get("total_tracks", 0),
        })
    return merged