import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_winners_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 16, 8, 13, 122772)),
        ),
    ]
