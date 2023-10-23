import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
import isodate
import datetime


class PlayList:

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"
        self.playlist = PlayList.get_service().playlists().list(id=self.__playlist_id, part='snippet', ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.playlist_videos = PlayList.get_service().playlistItems().list(playlistId=self.__playlist_id,
                                                                           part='snippet, contentDetails',
                                                                           maxResults=50, ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = PlayList.get_service().videos().list(part='contentDetails, statistics',
                                                                    id=','.join(self.video_ids)).execute()

    @classmethod
    def get_service(cls):
        os.environ['YT_API_KEY'] = "AIzaSyDaIAl0rWZyaQ49BEF5gM7-W7c3Butbdms"
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __str__(self):
        return self.total_duration()

    def total_duration(self):
        durations = datetime.timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            durations += isodate.parse_duration(iso_8601_duration)
        return durations

    def show_best_video(self):
        count_likes = 0
        best_video_id = ""
        for video in self.video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > count_likes:
                best_video_id = video['id']
        return f"https://youtu.be/{best_video_id}"
