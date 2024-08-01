from django.urls import path
from .views import ArtistAPIViewSet,AlbomAPiView,SongsAPIView

urlpatterns=[
    path('artist/', ArtistAPIViewSet.as_view(),name='artist'),
    path('albom/',AlbomAPiView.as_view(),name='albom'),
    path('song/',SongsAPIView.as_view(),name='song')
    ]


