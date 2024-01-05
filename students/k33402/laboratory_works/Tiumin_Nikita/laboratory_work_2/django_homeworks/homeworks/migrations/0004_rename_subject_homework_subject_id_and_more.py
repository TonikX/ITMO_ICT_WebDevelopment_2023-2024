# Generated by Django 4.2.6 on 2023-10-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0003_alter_user_is_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='subject',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='teacher',
            new_name='teacher_id',
        ),
        migrations.RenameField(
            model_name='homeworkgrade',
            old_name='homework_submission',
            new_name='homework_submission_id',
        ),
        migrations.RenameField(
            model_name='homeworksubmission',
            old_name='homework',
            new_name='homework_id',
        ),
        migrations.RenameField(
            model_name='homeworksubmission',
            old_name='student',
            new_name='student_id',
        ),
    ]
