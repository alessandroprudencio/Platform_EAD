# Generated by Django 2.1.7 on 2019-04-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190413_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, upload_to='courses/image'),
        ),
    ]