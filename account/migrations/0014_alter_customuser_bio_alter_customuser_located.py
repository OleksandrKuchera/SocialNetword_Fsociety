# Generated by Django 5.0.3 on 2024-04-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_customuser_bio_alter_customuser_located'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='located',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
