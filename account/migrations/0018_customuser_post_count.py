# Generated by Django 5.0.3 on 2024-04-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_customuser_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='post_count',
            field=models.IntegerField(default=0),
        ),
    ]