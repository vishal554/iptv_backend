from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from api.iptv.serializers import ChannelSerializer, CountrySerializer, StreamSerializer
from iptv.models import Channel, Country, Stream
from rest_framework import generics
from django.db.models import Q

from utils.helpers import error_response, success_response


class ChannelAPIView(generics.ListAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        country_code = self.request.query_params.get('country_code', None)
        subdivision = self.request.query_params.get('subdivision', None)  
        city = self.request.query_params.get('city', None)
        broadcast_area = self.request.query_params.get('broadcast_area', None)
        languages = self.request.query_params.get('languages', None)
        categories = self.request.query_params.get('categories', None)
        is_nsfw = self.request.query_params.get('is_nsfw', "false")
        is_nsfw = True if is_nsfw == 'true' else False
        subdivision = None if subdivision == '' else subdivision

        return Channel.objects.filter(Q(country__code=country_code) & Q(subdivision__code=subdivision) &
                                      Q(is_nsfw=is_nsfw))

class StreamAPIView(generics.ListAPIView):
    serializer_class = StreamSerializer
    
    def get_queryset(self):
        uid = self.kwargs.get('channel')
        print('Stream.objects.filter(channel__id=uid)', uid, Stream.objects.filter(channel__id=uid).count())
        return Stream.objects.filter(channel__id=uid)
    
    
class CountryAPIView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    

class ChannelViewSet(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    def get_channels_of_country(self, request, country_code, **kwargs):
        serializer = ChannelSerializer(
            data=request.data, context={'request': request, 'kwargs': kwargs, 'country_code': country_code})
        if not serializer.is_valid():
            return error_response(status=HTTP_400_BAD_REQUEST, msg="error occured", data=serializer.errors)
        else:
            return success_response(status=HTTP_200_OK,
                                    msg="API to get all channels of a single country",
                                    data=serializer.data)

    def get_stream(self, request, channel_id, **kwargs):
        serializer = StreamSerializer(
            data=request.data, context={'request': request, 'kwargs': kwargs})
        if not serializer.is_valid():
            return error_response(status=HTTP_400_BAD_REQUEST, msg="error occured", data=serializer.errors)
        else:
            return success_response(status=HTTP_200_OK,
                                    msg="API to verify  otp",
                                    data=serializer.data)
