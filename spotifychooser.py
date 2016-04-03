##import unittest

import spotipy

##clim = {
##    "danceability" : 0.366,
##    "energy" : 0.963,
##    "key" : 11,
##    "loudness" : -5.301,
##    "mode" : 0,
##    "speechiness" : 0.142,
##    "acousticness" : 0.000273,
##    "instrumentalness" : 0.0122,
##    "liveness" : 0.115,
##    "valence" : 0.212,
##    "tempo" : 137.114,
##    "type" : "audio_features",
##    "id" : "7ouMYWpwJ422jRcDASZB7P",
##    "uri" : "spotify:track:7ouMYWpwJ422jRcDASZB7P",
##    "track_href" : "https://api.spotify.com/v1/tracks/7ouMYWpwJ422jRcDASZB7P",
##    "analysis_url" : "http://echonest-analysis.s3.amazonaws.com/TR/EKRQaQmj3oVgxmhikP2Kx2cRkxwVujI8d_aIe4q3fC--3HVSRY8cDTGJUAnNxoAEgGjv3yK_KUHBqV644=/3/full.json?AWSAccessKeyId=AKIAJRDFEY23UEVW42BQ&Expires=1459622447&Signature=St0mLXTL/oy35kZXDUgIjypuyxo%3D",
##    "duration_ms" : 366213,
##    "time_signature" : 4
##}
##song1={
##    "danceability" : 0.602,
##    "energy" : 0.905,
##    "key" : 2,
##        "loudness" : -4.046,
##        "mode" : 1,
##        "speechiness" : 0.0775,
##        "acousticness" : 0.000202,
##        "instrumentalness" : 0.0640,
##        "liveness" : 0.117,
##        "valence" : 0.436,
##        "tempo" : 128.019,
##        "type" : "audio_features",
##        "id" : "4VqPOruhp5EdPBeR92t6lQ",
##        "uri" : "spotify:track:4VqPOruhp5EdPBeR92t6lQ",
##        "track_href" : "https://api.spotify.com/v1/tracks/4VqPOruhp5EdPBeR92t6lQ",
##        "analysis_url" : "http://echonest-analysis.s3.amazonaws.com/TR/u7X79QAoA7BbONklFpvFCOTtaPbWCeWakqZxiyU4za75wHddFWLMJZacQRplMUGc4ofuDEGgV91PRYh20=/3/full.json?AWSAccessKeyId=AKIAJRDFEY23UEVW42BQ&Expires=1459622447&Signature=yHBljwTOAAJVKthY/1kxsIvJIvM%3D",
##        "duration_ms" : 304840,
##        "time_signature" : 4
##    }
##song2={
##        "danceability" : 0.585,
##        "energy" : 0.842,
##        "key" : 9,
##        "loudness" : -5.883,
##        "mode" : 0,
##        "speechiness" : 0.0556,
##        "acousticness" : 0.00242,
##        "instrumentalness" : 0.00686,
##        "liveness" : 0.0866,
##        "valence" : 0.437,
##        "tempo" : 118.211,
##        "type" : "audio_features",
##        "id" : "2takcwOaAZWiXQijPHIx7B",
##        "uri" : "spotify:track:2takcwOaAZWiXQijPHIx7B",
##        "track_href" : "https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B",
##        "analysis_url" : "http://echonest-analysis.s3.amazonaws.com/TR/ksgbYAlncW_bVSXjI4AQrzOBtuvH1odjck8NTEGyeK67ADIa_4KAfB2S5VDeXNqDV_xWt7KSWJw2KIyiI=/3/full.json?AWSAccessKeyId=AKIAJRDFEY23UEVW42BQ&Expires=1459622447&Signature=W6VRgXUADsefpiuowqslKmoGYnA%3D",
##        "duration_ms" : 237040,
##        "time_signature" : 4
##    }
##atts = { "audio_features" : [ clim, song1, song2 ]}



def energies(alist):
    """create a list of the energies of the songs"""
    list_of_tracks = alist
    lenergies=[]
    for i in list_of_tracks:
        lenergies.append(i["energy"])
    return lenergies

def dances(alist):
    """create a list of the danceabilities of the songs"""
    list_of_tracks = alist
    ldances=[]
    for i in list_of_tracks:
        ldances.append(i["danceability"])
    return ldances

def tempos(alist):
    """create a list of the tempos of the songs"""
    list_of_tracks = alist
    ltempos=[]
    for i in list_of_tracks:
        ltempos.append(i["tempo"])
    return ltempos

##class AttribsTests(unittest.TestCase):
##    """tests the attribute list funcitons"""
##    def test_energies(self):
##        self.assertEqual(energies(atts["audio_features"]),[0.963, 0.905, 0.842])
##    def test_dances(self):
##        self.assertEqual(dances(atts["audio_features"]),[.366,.602,.585])
##    def test_tempos(self):
##        self.assertEqual(tempos(atts["audio_features"]),[137.114,128.019,118.211])

def climax(alist):
    """find which track is the 'climax' (dance and energy, tempo)"""
    list_of_tracks = alist
    for i in range(0,len(list_of_tracks)):
        if max(dances(alist))==(dances(alist)[i]):
            dancei=i
        if (max(energies(alist))==(energies(alist)[i])):
            energyi=i
    if (dancei == energyi):
        lclimax=list_of_tracks[dancei]
    else:
        if ((list_of_tracks[dancei])["tempo"] >
            (list_of_tracks[energyi])["tempo"]):
            lclimax=list_of_tracks[dancei]
        elif ((list_of_tracks[dancei])["tempo"] <
              (list_of_tracks[energyi])["tempo"]):
            lclimax=list_of_tracks[energyi]
        else: lclimax=list_of_tracks[dancei]
    return lclimax

def climaxorder(alist):
    """orders the list in terms of climax-ness"""
    list_of_tracks = alist
    climorder = []
    while len(list_of_tracks) > 0:
        climorder.append(climax(list_of_tracks))
        list_of_tracks.remove(climax(list_of_tracks))
    return climorder

def playlistmaker(alist):
    blist = climaxorder(alist)
    clist = blist.copy()
    climaxs = clist[0]
    climl = blist[1:]
    playrising = []
    playfalling = []
    for i in range(0,len(climl)):
        if i % 3 == 0:
            playfalling.append(climl[i])
        else:
            playrising.append(climl[i])
    playrising.reverse()
    playrising.append(climaxs)
    playlist = playrising + playfalling
    return playlist

def idlist(alist):
    """create a list of the ids of the songs"""
    list_of_tracks = playlistmaker(alist)
    lids=[]
    for i in list_of_tracks:
        lids.append(i["id"])
    return lids   


##class ClimaxTests(unittest.TestCase):
##    """tests the functions involving climax"""
##    def test_climaxorder(self):
##        self.assertEqual(climaxorder(atts["audio_features"]),[clim,song1,song2])
##    def test_climax(self):
##        self.assertEqual(climax(atts["audio_features"]),clim)
##    def test_playlistmaker(self):
##        self.assertEqual(playlistmaker([song1,song2,clim]),[song2, clim, song1])
##    def test_idlist(self):
##        self.assertEqual(idlist([song1,song2,clim]), ["2takcwOaAZWiXQijPHIx7B","7ouMYWpwJ422jRcDASZB7P","4VqPOruhp5EdPBeR92t6lQ"])


def plistTotracks(uid,pid):
    user_playlist_tracks(uid, playlist_id=pid, fields=id)

def tracksToplist(uid,pid,trackids):
    user_playlist_replace_tracks(uid, pid, trackids)

def main(uid,pid):
    tracksToplist(uid, pid, idlist(audio_features(plistTotracks(uid,pid)))["audio_features"])

##if __name__ == '__main__':
##                         unittest.main()
