# Generated by Django 5.0.3 on 2024-03-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_friendship_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='account_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]