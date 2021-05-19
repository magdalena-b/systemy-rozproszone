from api.serializers import SongSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from django.core.serializers import serialize, json
import json
import requests

class SearchSongView(generics.CreateAPIView):
    
    serializer_class = SongSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            song = serializer.get_or_create(serializer.validated_data)

            title = song.title.replace(' ', '%20')
            song_url = 'https://some-random-api.ml/lyrics?title=' + title
            data = json.loads(requests.get(song_url).content)
            song.lyrics = data['lyrics']

        else:
            song = None
        
        return render(request, "show_song.html", {'song': song})




    