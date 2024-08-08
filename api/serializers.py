from .models import Albom,Artist,Songs
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('id','first_name','last_name','username','create_at')


class AlbomSerializer(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model=Albom
        fields=('id','title','artist')


class SongsSerializer(serializers.ModelSerializer):
    albom=AlbomSerializer()
    class Meta:
        model=Songs
        fields=('title','albom')



# mobile application

class ArtistSerializerMobile(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('first_name','last_name','username')

class AlbomSerializerMobile(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model=Albom
        fields=('title','artist')

class SongsSerializerMobile(serializers.ModelSerializer):
    albom=AlbomSerializer()
    class Meta:
        model=Songs
        fields=('title','albom')




# telebot application

class ArtistSerializerBot(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('first_name','last_name','username')

class AlbomSerializerBot(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model=Albom
        fields=('title','artist')

class SongsSerializerBot(serializers.ModelSerializer):
    albom=AlbomSerializer()
    class Meta:
        model=Songs
        fields=('title','albom')


# Web application

class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('first_name','last_name','username')

class AlbomSerializerWeb(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model=Albom
        fields=('title','artist')

class SongsSerializerWeb(serializers.ModelSerializer):
    albom=AlbomSerializer()
    class Meta:
        model=Songs
        fields=('title','albom')


