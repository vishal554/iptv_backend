"""
Import json data from URL to Datababse
"""
import requests
import json
from iptv.models import Country, Language
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://iptv-org.github.io/api/countries.json'  # URL to import from


class Command(BaseCommand):
    def import_country(self, data):
        code = data.get('code', None)
        name = data.get('name', None)
        flag = data.get('flag', None)
        languages = data.get('languages', None)
        try:
            country, created = Country.objects.get_or_create(
            code=code,
            name=name,
            flag=flag
            )
            if created:
                for language_code in languages:
                    language = Language.objects.get(code=language_code)
                    country.languages.add(language)
                country.save()
            print(f"\country, {country}, has been saved.")
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this country: {}\n{}".format(
                code, str(ex))
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
            self.import_country(data_object)
