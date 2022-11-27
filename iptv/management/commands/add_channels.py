"""
Import json data from URL to Datababse
"""
import requests
import json
from iptv.models import Category, Channel, Country, Language, Region, SubDivision
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://iptv-org.github.io/api/channels.json'  # URL to import from


class Command(BaseCommand):
    def import_channel(self, data):
        id = data.get('id', None)
        name = data.get('name', None)
        alt_name = data.get('alt_name', None)
        network = data.get('network', None)
        owners = data.get('owners', None)
        country = data.get('country', None)
        subdivision = data.get('subdivision', None)
        city = data.get('city', None)
        broadcast_area = data.get('broadcast_area', None)
        languages = data.get('languages', None)
        categories = data.get('categories', None)
        is_nsfw = data.get('is_nsfw', None)
        launched = data.get('launched', None)
        closed = data.get('closed', None)
        replaced_by = data.get('replaced_by', None)
        website = data.get('website', None)
        logo = data.get('logo', None)
        
        try:
            channel, created = Channel.objects.get_or_create(
            id=id,
            name=name,
            alt_name=alt_name,
            network=network,
            owners=owners,
            city=city,
            broadcast_area=broadcast_area,
            is_nsfw=is_nsfw,
            launched=launched,
            closed=closed,
            replaced_by=replaced_by,
            website=website,
            logo=logo
            )
            if created:
                subdivision = SubDivision.objects.filter(code=subdivision).first()
                if subdivision: 
                    channel.subdivision = subdivision
                    
                country = Country.objects.filter(code=country).first()
                if country:
                    channel.country = country
                
                for language_code in languages:
                    language = Language.objects.get(code=language_code)
                    channel.languages.add(language)
                    
                for category_code in categories:
                    category = Category.objects.get(id=category_code)
                    channel.categories.add(category)
                    
                channel.save()
            print(f"channel {channel}, has been saved.")
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this channel: {}\n{}".format(
                id, str(ex))
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
            self.import_channel(data_object)
