import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

# import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        os.environ['YT_API_KEY'] = "AIzaSyDaIAl0rWZyaQ49BEF5gM7-W7c3Butbdms"
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        data = youtube.channels().list(id='UC-OVMPlMA3-YCIeg4z5z23A', part='snippet,statistics').execute()
        print(json.dumps(data, indent=2, ensure_ascii=False))


