from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('', SearchSongView.as_view(), name='search-song')
]






