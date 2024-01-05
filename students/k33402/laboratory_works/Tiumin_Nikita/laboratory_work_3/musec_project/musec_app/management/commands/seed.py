# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from musec_app.models import DefaultFilePath, FileType, File, Artist, Song, File, Playlist
from django.core.exceptions import ObjectDoesNotExist
import random


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        # parser.add_argument('--mode', type=str, help="Mode")
        pass

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed()
        self.stdout.write('done.')


def create_files():
    default_files = [
        {
            'path': DefaultFilePath.FAVORITE_PLAYLIST_COVER,
            'type': FileType.IMAGE,
        }
    ]

    for item in default_files:
        try:
            if File.objects.filter(file=item['path']).get():
                continue
        except ObjectDoesNotExist:
            pass
        file = File(
            file=item['path'],
            type=item['type'],
        )
        file.save()


def seed_test_data():
    artists = [
        {
            'name': 'TnxSoMch',
            'avatar': None,
            'songs': [
                {
                    'name': 'Spit in my face',
                    'audio': 'simf.mp3',
                    'cover': 'simfc.jpg',
                }
            ],
        },
        {
            'name': 'Nirvana',
            'avatar': None,
            'songs': [
                {
                    'name': 'Hear shaped box',
                    'audio': 'hsb.mp3',
                    'cover': 'hsbc.jpg',
                }
            ],
        },
        {
            'name': 'Black Sabbath',
            'avatar': None,
            'songs': [
                {
                    'name': 'Paranoid',
                    'audio': 'bs.mp3',
                    'cover': 'bsc.jpg',
                }
            ],
        },
        {
            'name': 'Mr. Kitty',
            'avatar': None,
            'songs': [
                {
                    'name': 'After dark',
                    'audio': 'ad.mp3',
                    'cover': 'adc.jpg',
                }
            ],
        },
        {
            'name': 'ATL',
            'avatar': None,
            'songs': [
                {
                    'name': 'Марабу',
                    'audio': 'marabu.mp3',
                    'cover': 'marabuc.jpg',
                }
            ],
        },
    ]

    for artist in artists:
        artist_model = Artist(
            name=artist['name'],
            avatar=artist['avatar'],
        )
        artist_model.save()
        for song in artist['songs']:
            cover = File(
                file='storage/' + song['cover'],
                type=FileType.IMAGE
            )
            cover.save()
            audio = File(
                file='storage/' + song['audio'],
                type=FileType.AUDIO
            )
            audio.save()
            song_model = Song(
                name=song['name'],
                cover=cover,
                audio=audio,
                artist=artist_model,
            )
            song_model.save()

    cover = File(
        file='storage/' + 'best.webp',
        type='image'
    )
    cover.save()
    playlist = Playlist(
        name='Most listened',
        cover=cover,
        user=None,
        is_public=True
    )
    playlist.save()
    playlist.songs.add(*list(Song.objects.all()))


def run_seed():
    create_files()
    seed_test_data()
