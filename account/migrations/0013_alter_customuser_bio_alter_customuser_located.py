# Generated by Django 5.0.3 on 2024-04-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='located',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
