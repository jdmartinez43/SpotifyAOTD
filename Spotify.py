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
BASE_SPOTIFY_ADDRESS = "https://api.spotify.com/v1"

# API keys can be generated from the developer Spotify account
SPOTIFY_API_KEY = ""
# name of the playlist to pull albums from
ALBUMS_PLAYLIST_NAME = "bums"
# id for ^
ALBUMS_PLAYLIST_URI = "7KTz9ojjRuT5A1QvMBxaqJ"  
# name of the playlist to add albums to 
AOTD_PLAYLIST_NAME = "[ae]otd22"
# id for ^
AOTD_PLAYLIST_URI = "3jtlrfQk8N9XAMzSJTraoL"

# Get Playlist Items Limit value
GET_PLAYLIST_ITEMS_LIMIT = 25
# Get Playlist Items Fields value
GET_PLAYLIST_ITEMS_FIELDS = "items(track(name,href,album(name,href)))"


# to work with api's 
# - encode your query params to be sent to the web API
# - issue an HTTP request to the URL and get the HTTP Response
# - parse the returned json response based on documentation


def buildPullURL(playlistURI: str) -> str:
    """
    Build url for pulling tracks from a playlist given query parameters. 

    :param playlistURI: a spotify playlist's URI value
    : 
    """

    # Query params in python can be built by creating a list of 
    # 2-tuple's. The first value is the query parameter name
    # and the second value is the value.
    # Query params reference: https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks
    # fields: filters out what values will be returned. Our current field values
    #         will create the format below
    # limit: the max amount of tracks that can get sent
    # 
    # Example:
    # {
    #   "track": {
    #     "album": {
    #       "href": "https://api.spotify.com/v1/albums/{album_uri}",
    #       "name": "Album Name"
    #     },
    #     "href": "https://api.spotify.com/v1/tracks/{song_uri}",
    #     "name": "Song Name"
    #   }
    # }
    queryParams = [
        ("fields", GET_PLAYLIST_ITEMS_FIELDS),
        ("limit", GET_PLAYLIST_ITEMS_LIMIT)
    ]
    return BASE_SPOTIFY_ADDRESS + "/playlists/" + playlistURI \
         + "/tracks?" + urllib.parse.urlencode(queryParams)

# submit requests to Spotify until we get the first url
def pullFirstAlbum():
    # for now, simply start with getting all tracks with the 
    # the same album id, starting from the 0th track
    pass

def insertIntoAOTD():
    pass


if __name__ == "__main__":
    url = buildPullURL(ALBUMS_PLAYLIST_NAME)
    print(url)