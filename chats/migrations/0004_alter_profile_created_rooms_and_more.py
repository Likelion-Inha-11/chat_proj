# Generated by Django 4.2.1 on 2023-07-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_alter_profile_created_rooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_rooms',
            field=models.ManyToManyField(blank=True, related_name='created_by', to='chats.room'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fixed_rooms',
            field=models.ManyToManyField(blank=True, related_name='fixed_for', to='chats.room'),
        ),
    ]