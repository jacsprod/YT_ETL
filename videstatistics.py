import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")

CHANNEL_HANDLE="MrBeast"

max_result=50

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
        
        playlistid=get_playlist_id() 



def get_video_ids(playlistid):
    
    video_ids=[]    
    pageToken=None
     
    base_url=f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_result}&playlistId={playlistid}&key={API_KEY}"  

    try:
        
        while True:
            
            url = base_url
            
            if pageToken:
                
                url+=f"&pageToken={pageToken}"
                
            response = requests.get(url)    
            
            response.raise_for_status()
            
            data=response.json()
            
            for item in data.get('items',[]):
                video_id = item['contentDetails']['videoId'] 
                
                video_ids.append(video_id)   
                
            pageToken =data.get("nextPageToken")
            
            if not pageToken:
                break    
            
        return video_ids    
        
    except requests.exceptions.RequestException as e:
        raise    

        
if  __name__ =="__main__":   

      playlistid=get_playlist_id()
    
      print(get_video_ids(playlistid))
    
    
   # print("get_playlist_id will be executed")
    
#else:
    #print("get_playlist_id won be executed ")   