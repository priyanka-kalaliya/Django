# Generated by Django 4.1.2 on 2022-10-12 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_rename_tittle_post_title_remove_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
