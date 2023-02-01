# Discogs.py
"""
Goal: collect all artists from a label and save the data	
"""

import ENV_VARS
import discogs_client

class Discogs:
    
    requestTokenURL = r'https://api.discogs.com/oauth/request_token'
    authorizeURL = r'https://www.discogs.com/oauth/authorize'
    accessTokenURL = r'https://api.discogs.com/oauth/access_token'

    def __init__(self):
        self.discogs = discogs_client.Client(
            "LabelArtists/0.1", 
            user_token=ENV_VARS.DISCOGS_USER_TOKEN
        )



    def getArtistsFromLabel(self,label):
        results = self.discogs.search(label=label)
        # return results.count
        # pages = []
        # page, resultCount = 1,  0
        # while resultCount < results.count:
        #     data = [item for item in results.page(page)]
        #     pages.append(data)
        #     resultCount += len(data)
        #     page += 1
        d = results.page(0)
        return set(a.name for a in d[0].artists)

    # def getLabelFromArtist(self, artist):
    #     return self.discogs.artist(artist)

    # searches for disenchanted. just to make sure i havent
    # gotten banned yet
    def live(self):
        print(self.discogs.release(20017387).images[0])
        # print( self.discogs.search("disenchanted").page(1) )

dc = Discogs()
# dc.live()
# labelFromArtist = dc.getLabelFromArtist("The Marias")

artistFromLabel = dc.getArtistsFromLabel("nice life recording company")
print(artistFromLabel)