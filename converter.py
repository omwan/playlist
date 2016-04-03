import spotipy

def plistTotracks(uid,pid):
    user_playlist_tracks(uid, playlist_id=pid, fields=id)

def tracksToplist(uid,pid,trackids):
    user_playlist_replace_tracks(uid, pid, trackids)
