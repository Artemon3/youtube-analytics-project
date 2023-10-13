import os
from src.channel import Channel
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        data = self.get_service().videos().list(id=self.video_id, part='snippet,statistics,contentDetails').execute()
        self.title = data['items'][0]['snippet']['title']
        self.url = data['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = data['items'][0]['statistics']['viewCount']
        self.like_count = data['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def get_service(cls):
        os.environ['YT_API_KEY'] = "AIzaSyDaIAl0rWZyaQ49BEF5gM7-W7c3Butbdms"
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        data = self.get_service().videos().list(id=self.video_id, part='snippet,statistics,contentDetails').execute()
        self.title = data['items'][0]['snippet']['title']
        self.url = data['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = data['items'][0]['statistics']['viewCount']
        self.like_count = data['items'][0]['statistics']['likeCount']
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'

