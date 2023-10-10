import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        data = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = data['items'][0]['snippet']['title']
        self.video_count = data['items'][0]['statistics']['videoCount']
        self.url = data['items'][0]['snippet']['thumbnails']['default']['url']
        self.description = data['items'][0]['snippet']['description']
        self.subscribers = data['items'][0]['statistics']['subscriberCount']
        self.view_count = data['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title}({self.url})'

    def __add__(self, other):
        return int(self.subscribers) + int(other.subscribers)

    def __sub__(self, other):
        return int(other.subscribers) - int(self.subscribers)

    def __gt__(self, other):
        return int(self.subscribers) > int(other.subscribers)

    def __ge__(self, other):
        return int(self.subscribers) >= int(other.subscribers)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        data = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        data1 = json.dumps(data, indent=2, ensure_ascii=False)
        print(data1)

    @classmethod
    def get_service(cls):
        os.environ['YT_API_KEY'] = "AIzaSyDaIAl0rWZyaQ49BEF5gM7-W7c3Butbdms"
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file):
        """
        Сохраняет данные экземпляра класса в файл
        """
        dict_to_write = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file, 'w') as fp:
            json.dump(dict_to_write, fp)
