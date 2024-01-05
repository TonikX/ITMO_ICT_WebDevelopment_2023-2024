from django.urls import path
from musec_app.views import auth
from musec_app.views import user
from musec_app.views import songs
from musec_app.views import files
from musec_app.views import playlists


urlpatterns = [
    #  Auth
    path('register', auth.register, name='auth.register'),
    path('login', auth.login, name='auth.login'),
    path('logout', auth.logout, name='auth.logout'),

    #  User
    path('me', user.me, name='user.me'),

    #  Songs
    path('songs', songs.index, name='songs.index'),
    path('songs/<int:song_id>/favorite', songs.toggle_favorite, name='songs.favorite'),
    path('songs/upload', songs.store, name='songs.store'),  # test

    #  Playlists
    path('playlists', playlists.index, name='playlists.index'),
    path('playlists/my', playlists.my, name='playlists.my'),

    #  Files
    path('files/audio/<str:filename>', files.download_audio, name='audio.download'),
    path('files/image/<str:filename>', files.download_image, name='image.download'),
]
