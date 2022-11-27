from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
    
    
    path('countries/', views.CountryAPIView.as_view(), name="get_countries"),
    path('channel/', views.ChannelAPIView.as_view(), name="get_channels"),
    path('stream/<str:channel>/', views.StreamAPIView.as_view(), name="get_stream"),
]