from api.serializers import SongSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from django.core.serializers import serialize, json

class SearchSongView(generics.CreateAPIView):
    
    serializer_class = SongSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            song = serializer.create(serializer.validated_data)
            print("songggggggggg")
            return Response(status = status.HTTP_200_OK)

        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)



    