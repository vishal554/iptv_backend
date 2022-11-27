from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('iptv/', include(('api.iptv.urls',
                              'api_iptv'), namespace="api_iptv")),
]