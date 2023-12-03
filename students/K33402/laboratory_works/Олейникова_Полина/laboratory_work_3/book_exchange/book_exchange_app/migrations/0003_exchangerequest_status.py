# Generated by Django 4.2.6 on 2023-12-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_exchange_app', '0002_alter_exchangerequest_book_offered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangerequest',
            name='status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('accepted', 'Accepted'), ('notconsidered', 'Not considered')], default='notconsidered', max_length=13),
        ),
    ]
