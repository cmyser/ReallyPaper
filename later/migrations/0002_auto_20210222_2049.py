# Generated by Django 3.1.7 on 2021-02-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('later', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
