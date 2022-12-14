# Generated by Django 4.1.2 on 2022-10-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('image', models.FileField(upload_to='pic')),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
