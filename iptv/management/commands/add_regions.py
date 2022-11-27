"""
Import json data from URL to Datababse
"""
import requests
import json
from iptv.models import Country, Language, Region
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://iptv-org.github.io/api/regions.json'  # URL to import from


class Command(BaseCommand):
    def import_region(self, data):
        code = data.get('code', None)
        name = data.get('name', None)
        countries = data.get('countries', None)
        try:
            region, created = Region.objects.get_or_create(
            code=code,
            name=name,
            )
            if created:
                for country_code in countries:
                    country = Country.objects.get(code=country_code)
                    region.countries.add(country)
                region.save()
            print(f"Region {region}, has been saved.")
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this region: {}\n{}".format(
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
            self.import_region(data_object)
