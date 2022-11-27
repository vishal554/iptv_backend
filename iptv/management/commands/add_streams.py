"""
Import json data from URL to Datababse
"""
import requests
import json
from iptv.models import Channel, Country, Language, Region, Stream
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://iptv-org.github.io/api/streams.json'  # URL to import from


class Command(BaseCommand):
    def import_stream(self, data):
        channel = data.get('channel', None)
        url = data.get('url', None)
        http_referrer = data.get('http_referrer', None)
        user_agent = data.get('user_agent', None)
        status = data.get('status', None)
        width = data.get('width', None)
        height = data.get('height', None)
        bitrate = data.get('bitrate', None)
        frame_rate = data.get('frame_rate', None)
        added_at = data.get('added_at', None)
        updated_at = data.get('updated_at', None)
        checked_at = data.get('checked_at', None)
        
        try:
            channel = Channel.objects.filter(id=channel).first()
            if channel: 
                stream, created = Stream.objects.get_or_create(
                    channel=channel,
                    url=url,
                    http_referrer=http_referrer,
                    user_agent=user_agent,
                    status=status,
                    height=height,
                    width=width,
                    bitrate=bitrate,
                    frame_rate=frame_rate,
                    added_at=added_at,
                    updated_at=updated_at,
                    checked_at=checked_at,
                )
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this stream: {}\n{}".format(
                channel, str(ex))
            print(msg)

    def handle(self, *args, **options):
        """
        Makes a GET request to the API.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        for data_object in data:
            self.import_stream(data_object)
