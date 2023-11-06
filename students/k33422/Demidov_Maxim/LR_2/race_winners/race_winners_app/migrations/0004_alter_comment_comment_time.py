import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("race_winners_app", "0003_alter_comment_comment_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 11, 5, 15, 43, 54, 907722)
            ),
        ),
    ]
