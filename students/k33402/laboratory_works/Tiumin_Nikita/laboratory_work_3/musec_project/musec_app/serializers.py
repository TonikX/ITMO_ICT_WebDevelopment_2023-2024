from rest_framework import serializers
from musec_app.models import File, Song


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    patronymic = serializers.CharField(max_length=255)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)
    patronymic = serializers.CharField(max_length=255, write_only=True, allow_blank=True, allow_null=True)

    profile = ProfileSerializer(read_only=True)


class UserAuthSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    name = serializers.CharField(max_length=255)
    # avatar_url = serializers.CharField(max_length=255)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file']


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    cover_url = serializers.ReadOnlyField()
    audio_url = serializers.ReadOnlyField()
    artist = ArtistSerializer(read_only=True)

    name = serializers.CharField(max_length=255)

    artist_id = serializers.IntegerField(write_only=True)
    audio = serializers.FileField(write_only=True)
    cover = serializers.FileField(write_only=True)


class PlaylistSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    name = serializers.CharField(max_length=255)
    cover_url = serializers.ReadOnlyField()

    songs = SongSerializer(read_only=True, many=True)
