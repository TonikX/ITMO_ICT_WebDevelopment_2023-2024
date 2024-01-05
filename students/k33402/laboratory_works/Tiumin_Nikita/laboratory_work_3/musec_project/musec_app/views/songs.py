from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view, authentication_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from musec_app.auth.authentication import AppTokenAuthentication
from musec_app.responses import api_response
from musec_app.serializers import UserSerializer, SongSerializer, FileSerializer
from musec_app.models import Song, File, FileType


@api_view(['GET'])
@authentication_classes([AppTokenAuthentication])
def index(request):
    filters = {}
    try:
        filters['name__icontains'] = request.GET['search']
    except MultiValueDictKeyError:
        pass
    songs = Song.objects.filter(**filters).all()
    return api_response.payload(SongSerializer(songs, many=True).data)


@api_view(['POST'])
@authentication_classes([AppTokenAuthentication])
@parser_classes([MultiPartParser])
def store(request):
    serializer = SongSerializer(data=request.data)
    if not serializer.is_valid():
        return api_response.validation_error(serializer.errors)
    data = serializer.validated_data

    #  todo transaction
    audio = File(
        file=data['audio'],
        type=FileType.AUDIO
    )
    audio.save()

    cover = File(
        file=data['cover'],
        type=FileType.IMAGE
    )
    cover.save()

    song_data = {
        'name': data['name'],
        'artist_id': data['artist_id'],
        'audio': audio,
        'cover': cover,
    }

    song = Song(**song_data)
    song.save()

    return api_response.success('Song successfully created')


@api_view(['POST'])
@authentication_classes([AppTokenAuthentication])
def toggle_favorite(request, song_id):
    song = Song.objects.filter(id=song_id).get()
    if not song:
        return api_response.not_found('Song was not found.')

    favorite_playlist = request.user.favorite_playlist

    if favorite_playlist.songs.filter(id=song_id).all().first():
        #  already liked
        favorite_playlist.songs.remove(song)
    else:
        favorite_playlist.songs.add(song)

    return api_response.success()
