# Generated by Django 5.0.3 on 2024-04-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_customuser_birth_date_alter_customuser_located'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, default='2024.01.01', null=True),
        ),
    ]
