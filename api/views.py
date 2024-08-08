from django.shortcuts import render
from .models import Albom,Artist,Songs
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtistSerializer,AlbomSerializer,SongsSerializer
from .serializers import AlbomSerializerMobile,ArtistSerializerMobile,SongsSerializerMobile
from .serializers import AlbomSerializerBot,ArtistSerializerBot,SongsSerializerBot
from .serializers import AlbomSerializerWeb,ArtistSerializerWeb,SongsSerializerWeb
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated


#                           ARTIST

class ArtistApiViewSet(ModelViewSet):
    artist=Artist.objects.all()
    serializer_class = ArtistSerializer

#                           ALBOM

class AlbomApiViewSet(ModelViewSet):
    albom=Albom.objects.all()
    serializer_class=AlbomSerializer

#                           SONGS

class SongsApiViewSET(ModelViewSet):
    song=Songs.objects.all()
    serializer_class=SongsSerializer



#                        mobile

class ArtistApiViewSetMobile(ModelViewSet):
    artist=Artist.objects.all()
    serializer_class = ArtistSerializerMobile
    permission_classes = [IsAdminUser, IsAuthenticated]

class AlbomApiViewSetMobile(ModelViewSet):
    albom=Albom.objects.all()
    serializer_class=AlbomSerializerMobile
    permission_classes = [IsAdminUser,IsAuthenticated]

class SongsApiViewSETMobile(ModelViewSet):
    song=Songs.objects.all()
    serializer_class=SongsSerializerMobile
    permission_classes = [IsAdminUser,IsAuthenticated]

#                        telebot

class ArtistApiViewSetBot(ModelViewSet):
    artist = Artist.objects.all()
    serializer_class = ArtistSerializerBot


class AlbomApiViewSetBot(ModelViewSet):
    albom = Albom.objects.all()
    serializer_class = AlbomSerializerBot


class SongsApiViewSETBot(ModelViewSet):
    song = Songs.objects.all()
    serializer_class = SongsSerializerBot

#                        Web

class ArtistApiViewSetWeb(ModelViewSet):
    artist = Artist.objects.all()
    serializer_class = ArtistSerializerWeb
    permission_classes = [IsAdminUser,IsAuthenticated]


class AlbomApiViewSetWeb(ModelViewSet):
    albom = Albom.objects.all()
    serializer_class = AlbomSerializerWeb
    permission_classes = [IsAdminUser,IsAuthenticated]


class SongsApiViewSETWeb(ModelViewSet):
    song = Songs.objects.all()
    serializer_class = SongsSerializerWeb
    permission_classes = [IsAdminUser, IsAuthenticated]