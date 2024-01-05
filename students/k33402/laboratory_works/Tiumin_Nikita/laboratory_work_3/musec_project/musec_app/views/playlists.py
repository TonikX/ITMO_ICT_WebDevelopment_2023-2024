from rest_framework.decorators import api_view, authentication_classes
from musec_app.auth.authentication import AppTokenAuthentication
from musec_app.responses import api_response
from musec_app.serializers import PlaylistSerializer
from musec_app.models import Playlist
from django.utils.datastructures import MultiValueDictKeyError


@api_view(['GET'])
@authentication_classes([AppTokenAuthentication])
def my(request):
    #  todo add playlists liked by user to the result
    playlists = Playlist.objects.filter(user_id=request.user.id, is_public=False).all()
    return api_response.payload(PlaylistSerializer(playlists, many=True).data)


@api_view(['GET'])
@authentication_classes([AppTokenAuthentication])
def index(request):
    filters = {
        'user_id': None,
        'is_public': True,
    }
    try:
        filters['name__icontains'] = request.GET['search']
    except MultiValueDictKeyError:
        pass

    playlists = Playlist.objects.filter(**filters).all()

    return api_response.payload(PlaylistSerializer(playlists, many=True).data)
