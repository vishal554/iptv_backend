
from rest_framework import exceptions, serializers
from iptv.models import Channel, Country, Language, Stream


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ["url", "status", "frame_rate", "updated_at"]


class ChannelSerializer(serializers.ModelSerializer):
    streams = StreamSerializer(many=True)
    class Meta:
        model = Channel
        fields = ['name', "country", "subdivision", "city", "languages", "categories", "is_nsfw", "logo", "streams"] 
    

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    class Meta:
        model = Country
        fields = "__all__"
