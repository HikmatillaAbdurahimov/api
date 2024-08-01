from django.shortcuts import render
from .models import Albom,Artist,Songs
from rest_framework.views import APIView
from .serializers import ArtistSerializer,AlbomSerializer
from rest_framework.response import Response


class ArtistAPIViewSet(APIView):
    def get(self,request):
        queryset=Artist.objects.all()
        serializer=ArtistSerializer(queryset,many=True)
        return Response(data=serializer.data)

class AlbomAPiView(APIView):
    def get(self,request):
        alboms=Albom.objects.all()
        albom_serializer=AlbomSerializer(alboms,many=True)
        return Response(data=albom_serializer.data)

class SongsAPIView(APIView):
    def get(self,request):
        songs=Songs.objects.all()
        serializer=AlbomSerializer(songs,many=True)
        return Response(data=serializer.data)





