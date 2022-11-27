from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, primary_key=True)


class Category(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)


class Country(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language, related_name='countries')


class SubDivision(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name='subdivisions')


class Region(models.Model):
    countries = models.ManyToManyField(Country, related_name='regions')
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)


class Channel(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    alt_name = models.CharField(max_length=100, null=True, blank=True)
    network = models.CharField(max_length=100, null=True, blank=True)
    owners = models.CharField(max_length=1000)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name='channels', null=True, blank=True)
    subdivision = models.ForeignKey(
        SubDivision, on_delete=models.PROTECT, related_name='channels', null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    broadcast_area = models.CharField(max_length=1000)
    languages = models.ManyToManyField(Language, related_name='channels')
    categories = models.ManyToManyField(Category, related_name='channels')
    is_nsfw = models.BooleanField()
    launched = models.DateField(null=True, blank=True)
    closed = models.DateField(null=True, blank=True)
    replaced_by = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    logo = models.URLField()


class Stream(models.Model):
    channel = models.ForeignKey(
        Channel, related_name='streams', on_delete=models.PROTECT)
    url = models.URLField()
    http_referrer = models.URLField(null=True, blank=True)
    user_agent = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bitrate = models.IntegerField(null=True, blank=True)
    frame_rate = models.FloatField(null=True, blank=True)
    added_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    checked_at = models.DateTimeField(null=True, blank=True)


class Guide(models.Model):
    channel = models.OneToOneField(
        Channel, on_delete=models.PROTECT, related_name='guide', primary_key=True)
    site = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    url = models.URLField


class BlockList(models.Model):
    channel = models.ForeignKey(
        Channel, on_delete=models.PROTECT, related_name='blocklist')
