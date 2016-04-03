import unittest
import spotipy


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

def get_ids_from_playlist(plist):
    list_of_tracks = alist["items"]
    idplist = []
    k=[]
    for i in list_of_tracks:
        k = i["tracks"]
        idsplist.append(k["id"])
    return idsplist


def plistTotracks(sp, uid,pid):
    return sp.user_playlist_tracks(uid, playlist_id=pid, fields='items(track(id))')

def track_ids_to_playlist(sp, uid,pid,trackids):
    """
    
    """
    return sp.user_playlist_replace_tracks(uid, pid, trackids)

def get_playlist_json(sp, uid, pid):
    """
    
    """
    return track_ids_to_playlist(sp, uid, pid,
                                 idlist(
                                     sp.audio_features(
                                         get_ids_from_playlist(
                                             plistTotracks(sp, uid,pid)))))

