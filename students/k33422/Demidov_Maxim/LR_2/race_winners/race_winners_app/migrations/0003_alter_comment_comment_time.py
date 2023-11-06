import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_winners_app', '0002_alter_comment_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 26, 16, 49, 14, 185549)),
        ),
    ]
