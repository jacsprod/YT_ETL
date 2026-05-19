import requests
import json

API_KEY="AIzaSyDTK_DEEJhruD9EhsASTjPb6P7KOrx6E3Y"
CHANNEL_HANDLE="MrBeast"

url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

response=requests.get(url)  

#print(response.text)
print(response.json)
#print(response.content)

data=response.json()

print(json.dumps(data,indent=4))


channel_items=data["items"][0]

channel_playlistid=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

print(channel_playlistid)

 