# Generated by Django 4.1.2 on 2022-10-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_student_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
    ]
