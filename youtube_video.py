""" from googleapiclient.discovery import build

def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey='AIzaSyCKYkRn06Dt3Qg2e1kV6gYyJQJEhIcADF4')
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()
    return response

video_id = 'dQw4w9WgXcQ'
details = get_video_details(video_id)


def print_video_details(details):
    title = details['items'][0]['snippet']['title']
    view_count = details['items'][0]['statistics']['viewCount']
    print(f'Title: {title}')
    print(f'View count: {view_count}')

print_video_details(details) """
from googleapiclient.discovery import build
import os

DEVELOPER_KEY = os.getenv("DEVELOPER_KEY", "")

def search_videos(query):
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    request = youtube.search().list(part='id', type='video', q=query, maxResults=5)
    response = request.execute()
    return response

query = 'python tutorials'
results = search_videos(query)
print(results)