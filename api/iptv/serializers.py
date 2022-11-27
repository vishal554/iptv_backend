
from rest_framework import exceptions, serializers
from iptv.models import Channel, Country, Language, Stream


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    class Meta:
        model = Country
        fields = "__all__"
