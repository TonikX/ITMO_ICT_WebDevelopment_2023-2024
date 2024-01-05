from django.db import models
from django.urls import reverse
from django.conf import settings


class User(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)

    @property
    def favorite_playlist(self):
        return self.playlists.first()

    #  profile
    #  api_tokens
    #  playlists


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    patronymic = models.CharField(max_length=255, blank=True, null=True)

    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')


class ApiToken(models.Model):
    token = models.CharField(max_length=255, blank=False, null=False, unique=True)

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='api_tokens')

###################


class FileType(models.TextChoices):
    AUDIO = 'audio', 'audio'
    VIDEO = 'video', 'video'
    IMAGE = 'image', 'image'


class DefaultFilePath(models.TextChoices):
    FAVORITE_PLAYLIST_COVER = 'storage/default_playlist_cover.jpg', 'storage/default_playlist_cover.jpg'


class File(models.Model):
    file = models.FileField(upload_to='storage/')
    type = models.CharField(
        max_length=5,
        choices=FileType.choices
    )

    @property
    def filename(self):
        return str(self.file).split('storage/')[1]

    # path = models.CharField(max_length=255)
    # extension = models.CharField(max_length=255)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, related_name='+')

    #  songs
    #  albums


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True, related_name='songs')
    audio = models.ForeignKey(File, on_delete=models.RESTRICT, null=False, related_name='+')
    cover = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, related_name='+')
    name = models.CharField(max_length=255)

    @property
    def cover_url(self):
        return settings.APP_URL + reverse('image.download', kwargs={'filename': self.cover.filename})

    @property
    def audio_url(self):
        return settings.APP_URL + reverse('audio.download', kwargs={'filename': self.audio.filename})


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    cover = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, related_name='+')
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='playlists')

    songs = models.ManyToManyField(Song)

    @property
    def cover_url(self):
        return settings.APP_URL + reverse('image.download', kwargs={'filename': self.cover.filename})

    @staticmethod
    def create_favorite_playlist_for_user(user):
        cover = File.objects.filter(file=DefaultFilePath.FAVORITE_PLAYLIST_COVER).get()
        playlist = Playlist(
            name='Favorite',
            cover=cover,
            is_public=False,
            user=user
        )
        playlist.save()


class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, related_name='+')
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT)

    songs = models.ManyToManyField(Song)


# class UserListenedTo(models.Model):  #  todo polymorphic
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     listened_type = models.CharField(max_length=10)  # 'song', 'playlist', or 'album'
#     listened_id = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
