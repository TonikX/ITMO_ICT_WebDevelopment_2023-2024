# Generated by Django 4.2.6 on 2023-10-28 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list_of_conferences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='authorregistration',
            name='author',
        ),
        migrations.RemoveField(
            model_name='authorregistration',
            name='conference',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='comment_text',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='location_description',
        ),
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_date',
        ),
        migrations.AddField(
            model_name='review',
            name='comment_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conference',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='participation_conditions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name='conference',
            name='topics',
        ),
        migrations.AlterField(
            model_name='review',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_of_conferences.conference'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='AuthorRegistration',
        ),
        migrations.AddField(
            model_name='registration',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_of_conferences.conference'),
        ),
        migrations.AddField(
            model_name='registration',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list_of_conferences.topic'),
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conference',
            name='topics',
            field=models.ManyToManyField(to='list_of_conferences.topic'),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('user', 'conference', 'topic')},
        ),
    ]
