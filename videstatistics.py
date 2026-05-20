import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")

CHANNEL_HANDLE="MrBeast"

def get_playlist_id():
    
    try:

        url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response=requests.get(url)  

        #print(response.text)
        #print(response.json)
        #print(response.content)
        
        response.raise_for_status()

        data=response.json()

        print(json.dumps(data,indent=4))


        channel_items=data["items"][0]

        channel_playlistid=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistid)
       
        return channel_playlistid
    
    except  requests.exceptions.RequestException as e:
        
        print("Error",e)
    
if  __name__ =="__main__":   

    get_playlist_id()
    
    print("get_playlist_id will be executed")
    
else:
    print("get_playlist_id won be executed")   