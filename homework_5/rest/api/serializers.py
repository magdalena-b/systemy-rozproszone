from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import *



class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('title', 'author')

    def create(self, validated_data):
        try:
            song = Song.objects.create(
                title = validated_data['title'],
                author = validated_data['author']
            )
            song.save()
            return song

        except Exception as e:
            print(e)
            return None