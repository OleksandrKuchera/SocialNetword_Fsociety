# Generated by Django 5.0.3 on 2024-04-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0002_remove_friend_date_added_alter_friend_friend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='isFollow',
            field=models.BooleanField(default=False),
        ),
    ]
