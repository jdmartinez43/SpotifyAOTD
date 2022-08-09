# Spotify.py
# 
# The basic functionality would be:
#    - for album A in albums:
#    - erase album A from albums
#    - if A is not in aotd_albums, 
#       - insert A into  and break
# 
# https://developer.spotify.com/documentation/general/guides/authorization/
# https://developer.spotify.com/documentation/general/guides/working-with-playlists/
# https://developer.spotify.com/documentation/general/guides/working-with-playlists/#reading-a-playlist
# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist
# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks
# https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist
# https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-tracks-playlist
# https://www.ics.uci.edu/~thornton/ics32/Notes/WebAPIs/
# https://developer.spotify.com/dashboard/applications/eef29dd55afb4fb5891cf0c688cb53f2

import json 
import urllib.parse
import urllib.request

# The base builder URL we use to interact with the Spotify API 
BASE_SPOTIFY_ADDRESS = "https://api.spotify.com" # "https://api.spotify.com/v1"

# API keys can be generated from the developer Spotify account
SPOTIFY_API_KEY = ""
# name of the playlist to pull albums from
ALBUMS_PLAYLIST = "bums"  
# name of the playlist to add albums to 
AOTD_PLAYLIST = "[ae]otd22"
# POST request URL
ADD_ITEMS_TO_PLAYLIST = "/playlists/" + AOTD_PLAYLIST + "/tracks"
# DELETE request URL
DELETE_REMOVE_PLAYLIST_ITEMS =  "/playlists/" + ALBUMS_PLAYLIST + "/tracks"

# to work with api's 
# - encode your query params to be sent to the web API
# - issue an HTTP request to the URL and get the HTTP Response
# - parse the returned json response based on documentation

# build url for pulling album
def buildPullURL():
    queryParams = [
        ()
    ]
    return BASE_SPOTIFY_ADDRESS

def pullFirstAlbum():
    # for now, simply start with getting all tracks with the 
    # the same album id, starting from the 0th track
    pass

def insertIntoAOTD():
    pass

