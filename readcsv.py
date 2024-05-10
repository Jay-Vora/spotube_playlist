import pandas as pd
from googleapiclient.discovery import build

data = pd.read_csv("track_info.csv")

tracks = data.track
youtube = build('youtube', 'v3', developerKey='AIzaSyCKYkRn06Dt3Qg2e1kV6gYyJQJEhIcADF4')
my_list =[]
for track in tracks:

    search_response = youtube.search().list(
        part="id",
        q=track,
        type='video',
        videoCategoryId='10', # for music category,
        videoDuration="short",
        maxResults=1
    ).execute()
    video_ids = [item['id']['videoId'] for item in search_response.get('items', []) if item['id'].get('videoId')]

    video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

    my_list.append(video_urls)

print(my_list)