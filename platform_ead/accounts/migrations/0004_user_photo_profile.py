# Generated by Django 2.1.7 on 2019-04-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190409_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo_profile',
            field=models.FileField(blank=True, upload_to='accounts/photo'),
        ),
    ]