# Generated by Django 5.1.3 on 2024-11-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_user_last_login_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
