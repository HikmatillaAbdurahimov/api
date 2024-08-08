
from .views import SongsApiViewSET,AlbomApiViewSet,ArtistApiViewSet
from .views import SongsApiViewSETWeb,AlbomApiViewSetWeb,ArtistApiViewSetWeb
from .views import SongsApiViewSETMobile,AlbomApiViewSetMobile,ArtistApiViewSetMobile
from .views import SongsApiViewSETBot,AlbomApiViewSetBot,ArtistApiViewSetBot
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path,re_path,include
from rest_framework import routers

schema_view=get_schema_view(
    openapi.Info(
        title='spotify API docs',
        default_version='v1',
        description='API documentation',
        terms_of_service='https://www.gogle.com/policie/terms/',
        contact=openapi.Contact(email='contact@yourapi.local'),
        license=openapi.License(name='BSD license')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
roter=routers.DefaultRouter()
roter.register(r'song/',SongsApiViewSET,basename='song')
roter.register(r'albom/',AlbomApiViewSet,basename='albom')
roter.register(r'artist/',ArtistApiViewSet,basename='artist')

#                                MOBILE

roter.register(r'artist-mobile/',ArtistApiViewSetMobile,basename='artist-mobile')
roter.register(r'albom-mobile/',AlbomApiViewSetMobile,basename='albom-mobile')
roter.register(r'song-mobile/',SongsApiViewSETMobile,basename='song-mobile')

#                                WEB

roter.register(r'artist-web/',ArtistApiViewSetWeb,basename='artist-web')
roter.register(r'albom-web/',AlbomApiViewSetWeb,basename='albom-web')
roter.register(r'song-web/',SongsApiViewSETWeb,basename='song-web')

#                                BOT

roter.register(r'artist-bot/',ArtistApiViewSetBot,basename='artist-bot')
roter.register(r'albom-bot/',AlbomApiViewSetBot,basename='albom-bot')
roter.register(r'song-bot/',SongsApiViewSETBot,basename='song-bot')

urlpatterns=[
    path('',include(roter.urls)),
    path('artist-web/api_auth/',include('rest_framework.urls')),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]


