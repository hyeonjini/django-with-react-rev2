# Generated by Django 4.1 on 2022-10-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_gender_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='accounts/avatar/%Y/%m/%d'),
        ),
    ]
