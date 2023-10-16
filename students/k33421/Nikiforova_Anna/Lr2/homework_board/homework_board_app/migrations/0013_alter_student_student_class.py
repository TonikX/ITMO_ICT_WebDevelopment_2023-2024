# Generated by Django 4.2.5 on 2023-10-07 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homework_board_app", "0012_alter_homework_date_of_issue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_class",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="homework_board_app.class",
            ),
        ),
    ]
